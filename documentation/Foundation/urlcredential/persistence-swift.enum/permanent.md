# URLCredential.Persistence.permanent

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

The credential should be stored in the keychain.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case permanent
```

```c
NSURLCredentialPersistencePermanent
```

## See Also

### Persistence strategies
- [URLCredential.Persistence.none](./none.md)
  The credential should not be stored.
- [URLCredential.Persistence.forSession](./forsession.md)
  The credential should be stored only for this session.
- [URLCredential.Persistence.synchronizable](./synchronizable.md)
  The credential should be stored permanently in the keychain, and in addition should be distributed to other devices based on the owning Apple ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredential/persistence-swift.enum/permanent)*