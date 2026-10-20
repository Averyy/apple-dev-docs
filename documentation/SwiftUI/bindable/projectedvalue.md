# projectedValue

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The bindable wrapper for the object that creates bindings to its properties using dynamic member lookup.

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
var projectedValue: Bindable<Value> { get }
```

## See Also

### Getting the value
- [var wrappedValue: Value](./wrappedvalue.md)
  The wrapped object.
- [subscript<Subject>(dynamicMember _: ReferenceWritableKeyPath<Value, Subject>) -> Binding<Subject>](./subscript%28dynamicmember%29.md)
  Returns a binding to the value of a given key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/bindable/projectedvalue)*