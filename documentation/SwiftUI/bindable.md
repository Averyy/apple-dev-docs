# Bindable

**Framework**: SwiftUI  
**Kind**: struct

A property wrapper type that supports creating bindings to the mutable properties of observable objects.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@dynamicMemberLookup
@propertyWrapper struct Bindable<Value>
```

#### Overview

Use this property wrapper to create bindings to mutable properties of a data model object that conforms to the [`Observable`](https://developer.apple.com/documentation/Observation/Observable) protocol. For example, the following code wraps the `book` input with `@Bindable`. Then it uses a [`TextField`](textfield.md) to change the `title` property of a book, and a [`Toggle`](toggle.md) to change the `isAvailable` property, using the `$` syntax to pass a binding for each property to those controls.

```swift
@Observable
class Book: Identifiable {
    var title = "Sample Book Title"
    var isAvailable = true
}

struct BookEditView: View {
    @Bindable var book: Book
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        Form {
            TextField("Title", text: $book.title)

            Toggle("Book is available", isOn: $book.isAvailable)

            Button("Close") {
                dismiss()
            }
        }
    }
}
```

You can use the `Bindable` property wrapper on properties and variables to an [`Observable`](https://developer.apple.com/documentation/Observation/Observable) object. This includes global variables, properties that exists outside of SwiftUI types, or even local variables. For example, you can create a `@Bindable` variable within a view’s [`body`](view/body-8kl5o.md):

```swift
struct LibraryView: View {
    @State private var books = [Book(), Book(), Book()]

    var body: some View {
        List(books) { book in
            @Bindable var book = book
            TextField("Title", text: $book.title)
        }
    }
}
```

The `@Bindable` variable `book` provides a binding that connects [`TextField`](textfield.md) to the `title` property of a book so that a person can make changes directly to the model data.

Use this same approach when you need a binding to a property of an observable object stored in a view’s environment. For example, the following code uses the [`Environment`](environment.md) property wrapper to retrieve an instance of the observable type `Book`. Then the code creates a `@Bindable` variable `book` and passes a binding for the `title` property to a [`TextField`](textfield.md) using the `$` syntax.

```swift
struct TitleEditView: View {
    @Environment(Book.self) private var book

    var body: some View {
        @Bindable var book = book
        TextField("Title", text: $book.title)
    }
}
```

## Topics

### Creating a bindable value
- [init(Value)](bindable/init(_:).md)
  Creates a bindable object from an observable object.
- [init(wrappedValue: Value)](bindable/init(wrappedvalue:).md)
  Creates a bindable object from an observable object.
- [init(projectedValue: Bindable<Value>)](bindable/init(projectedvalue:).md)
  Creates a bindable from the value of another bindable.
### Getting the value
- [var wrappedValue: Value](bindable/wrappedvalue.md)
  The wrapped object.
- [var projectedValue: Bindable<Value>](bindable/projectedvalue.md)
  The bindable wrapper for the object that creates bindings to its properties using dynamic member lookup.
- [subscript<Subject>(dynamicMember _: ReferenceWritableKeyPath<Value, Subject>) -> Binding<Subject>](bindable/subscript(dynamicmember:).md)
  Returns a binding to the value of a given key path.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Managing user interface state](managing-user-interface-state.md)
  Encapsulate view-specific data within your app’s view hierarchy to make your views reusable.
- [struct State](state.md)
  A property wrapper type that can read and write a value managed by SwiftUI.
- [struct Binding](binding.md)
  A property wrapper type that can read and write a value owned by a source of truth.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/bindable)*