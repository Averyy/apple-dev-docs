# State()

**Framework**: SwiftUI  
**Kind**: macro  
**Role**: Macro

Creates a property that can read and write a value managed by SwiftUI.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@attached(accessor, names: named(init), named(get), named(set))
@attached(peer, names: prefixed(`_`), prefixed(__), prefixed(`$`)) macro State()
```

## Mentions

- [Managing user interface state](./managing-user-interface-state.md)

## Overview

> ❗ **Important**: When you build with Xcode 26 or earlier, the system uses the [`State`](./state.md) property wrapper instead.

Use state as the single source of truth for a given value type that you store in a view hierarchy. Create a state value in an [`App`](./app.md), [`Scene`](./scene.md), or [`View`](./view.md) by applying the `@State` attribute to a property declaration and providing an initial value. Declare state as private to prevent setting it in an initializer, which can conflict with the storage management that SwiftUI provides:

```swift
struct PlayButton: View {
    @State private var isPlaying: Bool = false // Create the state.

    var body: some View {
        Button(isPlaying ? "Pause" : "Play") { // Read the state.
            isPlaying.toggle() // Write the state.
        }
    }
}
```

SwiftUI manages the property’s storage. When the value changes, SwiftUI updates the parts of the view hierarchy that depend on the value. To access a state’s underlying value, you use its `wrappedValue` property. When you create state this way, you can access the wrapped value by referring directly to the state instance. The above example reads and writes the `isPlaying` state property’s wrapped value by referring to the property directly.

Declare state as private in the highest view in the view hierarchy that needs access to the value. Then share the state with any subviews that also need access, either directly for read-only access, or as a binding for read-write access. You can safely mutate state properties from any thread.

### Share state with subviews

If you pass a state property to a subview, SwiftUI updates the subview any time the value changes in the container view, but the subview can’t modify the value. To enable the subview to modify the state’s stored value, pass a [`Binding`](./binding.md) instead.

For example, you can remove the `isPlaying` state from the play button in the above example, and instead make the button take a binding:

```swift
struct PlayButton: View {
    @Binding var isPlaying: Bool // Play button now receives a binding.

    var body: some View {
        Button(isPlaying ? "Pause" : "Play") {
            isPlaying.toggle()
        }
    }
}
```

Then you can define a player view that declares the state and creates a binding to the state. Get the binding to the state value by accessing the state’s `projectedValue`, which you get by prefixing the property name with a dollar sign (`$`):

```swift
struct PlayerView: View {
    @State private var isPlaying: Bool = false // Create the state here now.

    var body: some View {
        VStack {
            PlayButton(isPlaying: $isPlaying) // Pass a binding.

            // ...
        }
    }
}
```

Initialize state by providing a default value in the state’s declaration, as in the above examples. Use state only for storage that’s local to a view and its subviews.

### Store observable objects

You can also store observable objects that you create with the [`Observable()`](../Observation/observable%28%29.md) macro in `State()`; for example:

```swift
@Observable
class Library {
    var name = "My library of books"
    // ...
}

struct ContentView: View {
    @State private var library = Library()

    var body: some View {
        LibraryView(library: library)
    }
}
```

A `State()` property instantiates its default value the first time SwiftUI instantiates the view.

### Share observable state objects with subviews

To share an [`Observable`](../Observation/observable.md) object stored in `State()` with a subview, pass the object reference to the subview. SwiftUI updates the subview anytime an observable property of the object changes, but only when the subview’s [`body`](./view/body-8kl5o.md) reads the property. For example, in the following code `BookView` updates each time `title` changes but not when `isAvailable` changes:

```swift
@Observable
class Book {
    var title = "A sample book"
    var isAvailable = true
}

struct ContentView: View {
    @State private var book = Book()

    var body: some View {
        BookView(book: book)
    }
}

struct BookView: View {
    var book: Book

    var body: some View {
        Text(book.title)
    }
}
```

`State()` properties provide bindings to their value. When storing an object, you can get a [`Binding`](./binding.md) to that object, specifically the reference to the object. This is useful when you need to change the reference stored in state in some other subview, such as setting the reference to `nil`:

```swift
struct ContentView: View {
    @State private var book: Book?

    var body: some View {
        DeleteBookView(book: $book)
            .task {
                book = Book()
            }
    }
}

struct DeleteBookView: View {
    @Binding var book: Book?

    var body: some View {
        Button("Delete book") {
            book = nil
        }
    }
}
```

However, passing a [`Binding`](./binding.md) to an object stored in `State()` isn’t necessary when you need to change properties of that object. For example, you can set the properties of the object to new values in a subview by passing the object reference instead of a binding to the reference:

```swift
struct ContentView: View {
    @State private var book = Book()

    var body: some View {
        BookCheckoutView(book: book)
    }
}

struct BookCheckoutView: View {
    var book: Book

    var body: some View {
        Button(book.isAvailable ? "Check out book" : "Return book") {
            book.isAvailable.toggle()
        }
    }
}
```

If you need a binding to a specific property of the object, pass either the binding to the object and extract bindings to specific properties where needed, or pass the object reference and use the [`Bindable`](./bindable.md) property wrapper to create bindings to specific properties. For example, in the following code `BookEditorView` wraps `book` with `@Bindable`. Then the view uses the `$` syntax to pass to a [`TextField`](./textfield.md) a binding to `title`:

```swift
struct ContentView: View {
    @State private var book = Book()

    var body: some View {
        BookView(book: book)
    }
}

struct BookView: View {
    let book: Book

    var body: some View {
        BookEditorView(book: book)
    }
}

struct BookEditorView: View {
    @Bindable var book: Book

    var body: some View {
        TextField("Title", text: $book.title)
    }
}
```

## See Also

### Creating and sharing view state
- [Managing user interface state](./managing-user-interface-state.md)
  Encapsulate view-specific data within your app’s view hierarchy to make your views reusable.
- [macro State<Value>(initialValue: Value)](./state%28initialvalue%29.md)
  Creates a property with an initial value that can read and write a value managed by SwiftUI.
- [macro State<Value>(wrappedValue: Value)](./state%28wrappedvalue%29.md)
  Creates a property with a wrapped value that can read and write a value managed by SwiftUI.
- [struct State](./state.md)
  A property wrapper type that can read and write a value managed by SwiftUI.
- [struct Bindable](./bindable.md)
  A property wrapper type that supports creating bindings to the mutable properties of observable objects.
- [struct Binding](./binding.md)
  A property wrapper type that can read and write a value owned by a source of truth.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/state())*