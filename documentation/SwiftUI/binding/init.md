# init(_:)

**Framework**: SwiftUI  
**Kind**: init

Creates a binding by projecting the base value to a hashable value.

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
init<V>(_ base: Binding<V>) where Value == AnyHashable, V : Hashable
```

## Parameters

- `base`: A   value to project to an   value.

## See Also

- [init(projectedValue: Binding<Value>)](binding/init(projectedvalue:).md)
  Creates a binding from the value of another binding.
- [init(get:set:)](binding/init(get:set:).md)
  Creates a binding with closures that read and write the binding value.
- [static func constant(Value) -> Binding<Value>](binding/constant(_:).md)
  Creates a binding with an immutable value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/binding/init(_:))*