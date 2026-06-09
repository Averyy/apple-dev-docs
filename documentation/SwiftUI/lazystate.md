# LazyState

**Framework**: SwiftUI  
**Kind**: struct

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
@frozen
struct LazyState<Value>
```

## Topics

### Creating a lazy state
- [init(initialValue: () -> Value)](lazystate/init(initialvalue:).md)
  Creates a state property that stores an initial wrapped value.
- [init()](lazystate/init.md)
  Creates a state property without an initial value.
### Getting the value
- [var projectedValue: Binding<Value>](lazystate/projectedvalue.md)
  A binding to the state value.
- [var wrappedValue: Value](lazystate/wrappedvalue.md)
  The underlying value referenced by the state variable.
### Enumerations
- [LazyState.Storage](lazystate/storage.md)

## Relationships

### Conforms To
- [DynamicProperty](dynamicproperty.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/lazystate)*