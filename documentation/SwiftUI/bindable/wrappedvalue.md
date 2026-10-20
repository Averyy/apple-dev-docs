# wrappedValue

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The wrapped object.

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
var wrappedValue: Value
```

## See Also

### Getting the value
- [var projectedValue: Bindable<Value>](./projectedvalue.md)
  The bindable wrapper for the object that creates bindings to its properties using dynamic member lookup.
- [subscript<Subject>(dynamicMember _: ReferenceWritableKeyPath<Value, Subject>) -> Binding<Subject>](./subscript%28dynamicmember%29.md)
  Returns a binding to the value of a given key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/bindable/wrappedvalue)*