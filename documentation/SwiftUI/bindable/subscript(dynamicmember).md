# subscript(dynamicMember:)

**Framework**: SwiftUI  
**Kind**: subscript  
**Role**: Instance Subscript

Returns a binding to the value of a given key path.

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
subscript<Subject>(dynamicMember keyPath: ReferenceWritableKeyPath<Value, Subject>) -> Binding<Subject> { get }
```

## See Also

### Getting the value
- [var wrappedValue: Value](./wrappedvalue.md)
  The wrapped object.
- [var projectedValue: Bindable<Value>](./projectedvalue.md)
  The bindable wrapper for the object that creates bindings to its properties using dynamic member lookup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/bindable/subscript(dynamicmember:))*