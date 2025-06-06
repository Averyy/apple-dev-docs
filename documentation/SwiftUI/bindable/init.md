# init(_:)

**Framework**: SwiftUI  
**Kind**: init

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

#### Discussion

This initializer is equivalent to [`init(wrappedValue:)`](bindable/init(wrappedvalue:).md), but is more succinct when when creating bindable objects nested within other expressions. For example, you can use the initializer to create a bindable object inline with code that declares a view that takes a binding as a parameter:

```swift
struct TitleEditView: View {
    @Environment(Book.self) private var book

    var body: some View {
        TextField("Title", text: Bindable(book).title)
    }
}
```

## See Also

- [init(wrappedValue: Value)](bindable/init(wrappedvalue:).md)
  Creates a bindable object from an observable object.
- [init(projectedValue: Bindable<Value>)](bindable/init(projectedvalue:).md)
  Creates a bindable from the value of another bindable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/bindable/init(_:))*