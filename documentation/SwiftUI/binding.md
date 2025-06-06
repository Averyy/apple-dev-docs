# Binding

**Framework**: Swiftui  
**Kind**: struct

A property wrapper type that can read and write a value owned by a source of truth.

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
@frozen
@propertyWrapper @dynamicMemberLookup struct Binding<Value>
```

## Mentions

- [Performing a search operation](performing-a-search-operation.md)
- [Understanding the navigation stack](understanding-the-composition-of-navigation-stack.md)
- [Managing user interface state](managing-user-interface-state.md)
- [Adding a search interface to your app](adding-a-search-interface-to-your-app.md)
- [Managing search interface activation](managing-search-interface-activation.md)

#### Overview

Use a binding to create a two-way connection between a property that stores data, and a view that displays and changes the data. A binding connects a property to a source of truth stored elsewhere, instead of storing data directly. For example, a button that toggles between play and pause can create a binding to a property of its parent view using the `Binding` property wrapper.

```swift
struct PlayButton: View {
    @Binding var isPlaying: Bool

    var body: some View {
        Button(isPlaying ? "Pause" : "Play") {
            isPlaying.toggle()
        }
    }
}
```

The parent view declares a property to hold the playing state, using the [`State`](state.md) property wrapper to indicate that this property is the value’s source of truth.

```swift
struct PlayerView: View {
    var episode: Episode
    @State private var isPlaying: Bool = false

    var body: some View {
        VStack {
            Text(episode.title)
                .foregroundStyle(isPlaying ? .primary : .secondary)
            PlayButton(isPlaying: $isPlaying) // Pass a binding.
        }
    }
}
```

When `PlayerView` initializes `PlayButton`, it passes a binding of its state property into the button’s binding property. Applying the `$` prefix to a property wrapped value returns its [`projectedValue`](state/projectedvalue.md), which for a state property wrapper returns a binding to the value.

Whenever the user taps the `PlayButton`, the `PlayerView` updates its `isPlaying` state.

A binding conforms to `Sendable` only if its wrapped value type also conforms to `Sendable`. It is always safe to pass a sendable binding between different concurrency domains. However, reading from or writing to a binding’s wrapped value from a different concurrency domain may or may not be safe, depending on how the binding was created. SwiftUI will issue a warning at runtime if it detects a binding being used in a way that may compromise data safety.

> **Note**: To create bindings to properties of a type that conforms to the [`Observable`](https://developer.apple.com/documentation/Observation/Observable) protocol, use the [`Bindable`](bindable.md) property wrapper. For more information, see [`Migrating from the Observable Object protocol to the Observable macro`](migrating-from-the-observable-object-protocol-to-the-observable-macro.md).

## Topics

### Creating a binding
- [init(_:)](binding/init(_:).md)
  Creates a binding by projecting the base value to a hashable value.
- [init(projectedValue: Binding<Value>)](binding/init(projectedvalue:).md)
  Creates a binding from the value of another binding.
- [init(get:set:)](binding/init(get:set:).md)
  Creates a binding with closures that read and write the binding value.
- [static func constant(Value) -> Binding<Value>](binding/constant(_:).md)
  Creates a binding with an immutable value.
### Getting the value
- [var wrappedValue: Value](binding/wrappedvalue.md)
  The underlying value referenced by the binding variable.
- [var projectedValue: Binding<Value>](binding/projectedvalue.md)
  A projection of the binding value that returns a binding.
- [subscript<Subject>(dynamicMember _: WritableKeyPath<Value, Subject>) -> Binding<Subject>](binding/subscript(dynamicmember:).md)
  Returns a binding to the resulting value of a given key path.
### Managing changes
- [var id: Value.ID](binding/id.md)
  The stable identity of the entity associated with this instance, corresponding to the `id` of the binding’s wrapped value.
- [func animation(Animation?) -> Binding<Value>](binding/animation(_:).md)
  Specifies an animation to perform when the binding value changes.
- [func transaction(Transaction) -> Binding<Value>](binding/transaction(_:).md)
  Specifies a transaction for the binding.
- [var transaction: Transaction](binding/transaction.md)
  The binding’s transaction.
### Default Implementations
- [Identifiable Implementations](binding/identifiable-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [DynamicProperty](dynamicproperty.md)
- [Identifiable](../Swift/Identifiable.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sendable](../Swift/Sendable.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [Managing user interface state](managing-user-interface-state.md)
  Encapsulate view-specific data within your app’s view hierarchy to make your views reusable.
- [struct State](state.md)
  A property wrapper type that can read and write a value managed by SwiftUI.
- [struct Bindable](bindable.md)
  A property wrapper type that supports creating bindings to the mutable properties of observable objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/SwiftUI/binding)*