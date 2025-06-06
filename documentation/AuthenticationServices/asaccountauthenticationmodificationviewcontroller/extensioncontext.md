# extensionContext

**Framework**: Authentication Services  
**Kind**: property

The context your account authentication modification extension uses to provide information to the system.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var extensionContext: ASAccountAuthenticationModificationExtensionContext { get }
```

## Mentions

- [Upgrading Account Security With an Account Authentication Modification Extension](upgrading-account-security-with-an-account-authentication-modification-extension.md)

#### Discussion

Your extension uses the extension context to communicate with the system during the upgrade process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationviewcontroller/extensioncontext)*