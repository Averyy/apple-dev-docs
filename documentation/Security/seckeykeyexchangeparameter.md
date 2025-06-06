# SecKeyKeyExchangeParameter

**Framework**: Security  
**Kind**: struct

The dictionary keys used to specify Diffie-Hellman key exchange parameters.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct SecKeyKeyExchangeParameter
```

#### Discussion

Use these constants as keys in the dictionary that you input to the [`SecKeyCopyKeyExchangeResult(_:_:_:_:_:)`](seckeycopykeyexchangeresult(_:_:_:_:_:).md) function as a means to refine the process of Diffie-Hellman key exchange.

## Topics

### Type Properties
- [static let requestedSize: SecKeyKeyExchangeParameter](seckeykeyexchangeparameter/requestedsize.md)
- [static let sharedInfo: SecKeyKeyExchangeParameter](seckeykeyexchangeparameter/sharedinfo.md)
### Initializers
- [init(rawValue: CFString)](seckeykeyexchangeparameter/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeykeyexchangeparameter)*