# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a bindable object from an observable object.

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
init(_ wrappedValue: Value)
```

Available when `Value` conforms to `Observable`.

## Discussion

This initializer is equivalent to [`init(wrappedValue:)`](./init%28wrappedvalue%29.md), but is more succinct when when creating bindable objects nested within other expressions. For example, you can use the initializer to create a bindable object inline with code that declares a view that takes a binding as a parameter:

```swift
struct TitleEditView: View {
    @Environment(Book.self) private var book

    var body: some View {
        TextField("Title", text: Bindable(book).title)
    }
}
```

## See Also

### Creating a bindable value
- [init(wrappedValue: Value)](./init%28wrappedvalue%29.md)
  Creates a bindable object from an observable object.
- [init(projectedValue: Bindable<Value>)](./init%28projectedvalue%29.md)
  Creates a bindable from the value of another bindable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/bindable/init(_:))*