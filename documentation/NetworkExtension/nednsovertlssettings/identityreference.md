# identityReference

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A persistent keychain reference to a keychain item containing the certificate and private key components of the DNS client credential.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var identityReference: Data? { get set }
```

```objc
@property (copy, nullable) NSData * identityReference;
```

## Discussion

The keychain item must have the [`kSecClassIdentity`](../../Security/ksecclassidentity.md) class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsovertlssettings/identityreference)*