# AccountExchangeOAuthObject

**Framework**: Device Management  
**Kind**: dictionary

The declaration for configuring OAuth authentication of an Exchange account.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.1+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object AccountExchangeOAuthObject
```

## Properties

- `Enabled` (boolean) *(required)*: If `true`, enables OAuth for this account.
- `SignInURL` (string): The URL that this account uses for signing in with OAuth. The system ignores this value unless `Enabled` is `true`. The system doesn’t use autodiscovery when a declaration contains this URL, so the declaration must also contain a `HostName`.
- `TokenRequestURL` (string): The URL that this account uses for token requests with OAuth. The system ignores this value unless `Enabled` is `true`.

## See Also

- [object AccountExchangeSMIMEObject](accountexchangesmimeobject.md)
  Settings for S/MIME.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/accountexchangeoauthobject)*