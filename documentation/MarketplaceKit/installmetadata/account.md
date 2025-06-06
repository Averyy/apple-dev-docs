# account

**Framework**: MarketplaceKit  
**Kind**: property

A user ID for the person installing the app.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
let account: String
```

#### Discussion

You set this value and the operating system sends it back to you as:

- The `login_hint` in the call to your authorization endpoint during re-authentication
- A parameter to your marketplace extension’s [`additionalHeaders(for:account:)`](marketplaceextension/additionalheaders(for:account:).md) callback

The system also groups apps in restore requests based on account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/installmetadata/account)*