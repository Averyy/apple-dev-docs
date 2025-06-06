# AnyKeyPath

**Framework**: Swift  
**Kind**: class

A type-erased key path, from any root type to any resulting value type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class AnyKeyPath
```

## Topics

### Type Properties
- [static var rootType: any Any.Type](anykeypath/roottype.md)
  The root type for this key path.
- [static var valueType: any Any.Type](anykeypath/valuetype.md)
  The value type for this key path.
### Default Implementations
- [CustomDebugStringConvertible Implementations](anykeypath/customdebugstringconvertible-implementations.md)
- [Equatable Implementations](anykeypath/equatable-implementations.md)
- [Hashable Implementations](anykeypath/hashable-implementations.md)

## Relationships

### Inherited By
- [PartialKeyPath](partialkeypath.md)
### Conforms To
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)

## See Also

- [class KeyPath](keypath.md)
  A key path from a specific root type to a specific resulting value type.
- [class PartialKeyPath](partialkeypath.md)
  A partially type-erased key path, from a concrete root type to any resulting value type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anykeypath)*