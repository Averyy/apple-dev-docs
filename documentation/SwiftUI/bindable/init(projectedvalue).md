# init(projectedValue:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a bindable from the value of another bindable.

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
init(projectedValue: Bindable<Value>)
```

Available when `Value` conforms to `Observable`.

## See Also

### Creating a bindable value
- [init(Value)](./init%28_%29.md)
  Creates a bindable object from an observable object.
- [init(wrappedValue: Value)](./init%28wrappedvalue%29.md)
  Creates a bindable object from an observable object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/bindable/init(projectedvalue:))*