# init(wrappedValue:)

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
init(wrappedValue: Value)
```

#### Discussion

You should not call this initializer directly. Instead, declare a property with the `@Bindable` attribute, and provide an initial value.

## See Also

- [init(Value)](bindable/init(_:).md)
  Creates a bindable object from an observable object.
- [init(projectedValue: Bindable<Value>)](bindable/init(projectedvalue:).md)
  Creates a bindable from the value of another bindable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/bindable/init(wrappedvalue:))*