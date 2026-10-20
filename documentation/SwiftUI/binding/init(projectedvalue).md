# init(projectedValue:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a binding from the value of another binding.

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
@export(implementation)
init(projectedValue: Binding<Value>)
```

## See Also

### Creating a binding
- [init(_:)](./init%28_%29.md)
  Creates a binding by projecting the base value to a hashable value.
- [init(get:set:)](./init%28get,set%29.md)
  Creates a binding with closures that read and write the binding value.
- [static func constant(Value) -> Binding<Value>](./constant%28_%29.md)
  Creates a binding with an immutable value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/binding/init(projectedvalue:))*