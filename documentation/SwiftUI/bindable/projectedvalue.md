# projectedValue

**Framework**: SwiftUI  
**Kind**: property

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

- [var wrappedValue: Value](bindable/wrappedvalue.md)
  The wrapped object.
- [subscript<Subject>(dynamicMember _: ReferenceWritableKeyPath<Value, Subject>) -> Binding<Subject>](bindable/subscript(dynamicmember:).md)
  Returns a binding to the value of a given key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/bindable/projectedvalue)*