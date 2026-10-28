# allowedClasses

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The set of coded classes allowed for secure coding.

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
var allowedClasses: Set<AnyHashable>? { get }
```

```objc
@property (copy, readonly, nullable) NSSet<Class> * allowedClasses;
```

## Discussion

Secure coders check this set of allowed classes before decoding objects, and all objects must implement the [`NSSecureCoding`](../nssecurecoding.md) protocol.

## See Also

### Secure Coding
- [var requiresSecureCoding: Bool](./requiressecurecoding.md)
  Indicates whether the archiver requires all archived classes to resist object substitution attacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/allowedclasses)*