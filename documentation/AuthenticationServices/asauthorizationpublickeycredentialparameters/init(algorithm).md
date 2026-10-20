# init(algorithm:)

**Framework**: Authentication Services  
**Kind**: init  
**Role**: Initializer

Creates the object with an algorithm.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
init(algorithm: ASCOSEAlgorithmIdentifier)
```

```objc
- (instancetype) initWithAlgorithm:(ASCOSEAlgorithmIdentifier) algorithm;
```

## Parameters

- `algorithm`: The algorithm to use for negitation between the authenticator and the relying party.

## See Also

### Getting the parameters
- [var algorithm: ASCOSEAlgorithmIdentifier](./algorithm.md)
  The algorithm to use for negitation between the authenticator and the relying party.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialparameters/init(algorithm:))*