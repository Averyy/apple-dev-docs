# init()

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a state property without an initial value.

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
init()
```

Available when `Value` conforms to `ExpressibleByNilLiteral`.

## Discussion

This initializer behaves like the [`init(wrappedValue:)`](./init%28wrappedvalue%29.md) initializer with an input of `nil`. See that initializer for more information.

## See Also

### Creating a state
- [init(wrappedValue: Value)](./init%28wrappedvalue%29.md)
  Creates a state property that stores an initial wrapped value.
- [init(initialValue: Value)](./init%28initialvalue%29.md)
  Creates a state property that stores an initial value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/state/init())*