# subscript(dynamicMember:)

**Framework**: SwiftUI  
**Kind**: subscript

Returns a binding to the resulting value of a given key path.

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
subscript<Subject>(dynamicMember keyPath: WritableKeyPath<Value, Subject>) -> Binding<Subject> { get }
```

#### Return Value

A new binding.

## Parameters

- `keyPath`: A key path to a specific resulting value.

## See Also

- [var wrappedValue: Value](binding/wrappedvalue.md)
  The underlying value referenced by the binding variable.
- [var projectedValue: Binding<Value>](binding/projectedvalue.md)
  A projection of the binding value that returns a binding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/binding/subscript(dynamicmember:))*