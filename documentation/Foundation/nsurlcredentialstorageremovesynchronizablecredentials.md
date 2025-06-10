# NSURLCredentialStorageRemoveSynchronizableCredentials

**Framework**: Foundation  
**Kind**: var

The corresponding value is an `NSNumber` object representing a Boolean value that indicates whether credentials which contain the [`URLCredential.Persistence.synchronizable`](urlcredential/persistence-swift.enum/synchronizable.md) attribute should be removed.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let NSURLCredentialStorageRemoveSynchronizableCredentials: String
```

#### Discussion

If the key is missing or the value is `@NO`, then no attempt will be made to remove such a credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlcredentialstorageremovesynchronizablecredentials)*