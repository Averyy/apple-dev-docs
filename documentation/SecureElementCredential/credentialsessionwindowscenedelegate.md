# CredentialSessionWindowSceneDelegate

**Framework**: SecureElementCredential  
**Kind**: protocol

Delegate to notify your `UIWindowScene` that a CredentialSession event has occurred.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
protocol CredentialSessionWindowSceneDelegate
```

## Mentions

- [Accessing and using secure element credentials](accessing-and-using-secure-element-credentials.md)

#### Overview

All files that refer to symbols defined here should never `import SwiftUI` Importing SwiftUI with UIKit will result in ambiguous symbols during compilation.

## Topics

### Handling events
- [func windowScene(UIWindowScene, didReceiveCredentialSessionWindowSceneEvent: CredentialSessionWindowSceneEvent)](credentialsessionwindowscenedelegate/windowscene(_:didreceivecredentialsessionwindowsceneevent:).md)
- [enum CredentialSessionWindowSceneEvent](credentialsessionwindowsceneevent.md)
  A CredentialSession event send to a `UIScene` or `UIWindowScene`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsessionwindowscenedelegate)*