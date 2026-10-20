# URLCredential.Persistence.synchronizable

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

The credential should be stored permanently in the keychain, and in addition should be distributed to other devices based on the owning Apple ID.

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
case synchronizable
```

```c
NSURLCredentialPersistenceSynchronizable
```

## See Also

### Persistence strategies
- [URLCredential.Persistence.none](./none.md)
  The credential should not be stored.
- [URLCredential.Persistence.forSession](./forsession.md)
  The credential should be stored only for this session.
- [URLCredential.Persistence.permanent](./permanent.md)
  The credential should be stored in the keychain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredential/persistence-swift.enum/synchronizable)*