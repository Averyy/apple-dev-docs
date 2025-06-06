# KeyPath

**Framework**: Swift  
**Kind**: class

A key path from a specific root type to a specific resulting value type.

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
class KeyPath<Root, Value>
```

#### Overview

The most common way to make an instance of this type is by using a key-path expression like `\SomeClass.someProperty`. For more information, see [`Key-Path Expressions`](https://developer.apple.comhttps://docs.swift.org/swift-book/ReferenceManual/Expressions.html#ID563) in .

## Relationships

### Inherits From
- [PartialKeyPath](partialkeypath.md)
### Inherited By
- [WritableKeyPath](writablekeypath.md)
### Conforms To
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)

## See Also

- [class PartialKeyPath](partialkeypath.md)
  A partially type-erased key path, from a concrete root type to any resulting value type.
- [class AnyKeyPath](anykeypath.md)
  A type-erased key path, from any root type to any resulting value type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keypath)*