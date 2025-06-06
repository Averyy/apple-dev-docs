# kSecSharedPassword

**Framework**: Security  
**Kind**: var

A dictionary key whose value is the shared password.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
let kSecSharedPassword: CFString
```

#### Discussion

The dictionary returned by the [`SecRequestSharedWebCredential(_:_:_:)`](secrequestsharedwebcredential(_:_:_:).md) function includes this key to provide you with the password.

You can also access the server’s URL and the user name from this dictionary. To access the server, use the [`kSecAttrServer`](ksecattrserver.md) constant. To access the user name, use the [`kSecAttrAccount`](ksecattraccount.md) constant. These constants are part of the [`Keychain services`](keychain-services.md) API, and in particular are listed among the [`Item attribute keys and values`](item-attribute-keys-and-values.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecsharedpassword)*