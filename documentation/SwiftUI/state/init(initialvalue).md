# init(initialValue:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a state property that stores an initial value.

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
init(initialValue value: Value)
```

## Discussion

This initializer has the same behavior as the [`init(wrappedValue:)`](./init%28wrappedvalue%29.md) initializer. See that initializer for more information.

## Parameters

- `value`: An initial value to store in the state property.

## See Also

### Creating a state
- [init(wrappedValue: Value)](./init%28wrappedvalue%29.md)
  Creates a state property that stores an initial wrapped value.
- [init()](./init%28%29.md)
  Creates a state property without an initial value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/state/init(initialvalue:))*