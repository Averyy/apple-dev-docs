# requiresSecureCoding

**Framework**: Foundation  
**Kind**: property

Indicates whether the archiver requires all archived classes to resist object substitution attacks.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var requiresSecureCoding: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if this coder requires secure coding; [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

Secure coders check a set of allowed classes before decoding objects, and all objects must implement the [`NSSecureCoding`](nssecurecoding.md) protocol.

## See Also

- [var allowsKeyedCoding: Bool](nscoder/allowskeyedcoding.md)
  A Boolean value that indicates whether the receiver supports keyed coding of objects.
- [var allowedClasses: Set<AnyHashable>?](nscoder/allowedclasses.md)
  The set of coded classes allowed for secure coding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/requiressecurecoding)*