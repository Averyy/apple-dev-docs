# init(initialValue:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an observed object with an initial value.

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
@MainActor
@export(implementation) @preconcurrency init(initialValue: ObjectType)
```

## Discussion

This initializer has the same behavior as the [`init(wrappedValue:)`](./init%28wrappedvalue%29.md) initializer. See that initializer for more information.

## Parameters

- `initialValue`: An initial value.

## See Also

### Creating an observed object
- [init(wrappedValue: ObjectType)](./init%28wrappedvalue%29.md)
  Creates an observed object with an initial wrapped value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/observedobject/init(initialvalue:))*