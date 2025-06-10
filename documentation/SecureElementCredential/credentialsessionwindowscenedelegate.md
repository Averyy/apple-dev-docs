# CredentialSessionWindowSceneDelegate

**Framework**: SecureElementCredential  
**Kind**: protocol

A protocol to notify a UIKit scene that a credential session event occurred.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
protocol CredentialSessionWindowSceneDelegate
```

## Mentions

- [Accessing and using secure element credentials](accessing-and-using-secure-element-credentials.md)

#### Overview

> ⚠️ **Warning**: Don’t import SwiftUI in any files that refer to symbols defined in this protocol. Importing SwiftUI and UIKit in the same file results in ambiguity during compilation.

## Topics

### Handling events
- [func windowScene(UIWindowScene, didReceiveCredentialSessionWindowSceneEvent: CredentialSessionWindowSceneEvent)](credentialsessionwindowscenedelegate/windowscene(_:didreceivecredentialsessionwindowsceneevent:).md)
  Informs your app that a credential session event initiated a UIKit scene creation.
- [enum CredentialSessionWindowSceneEvent](credentialsessionwindowsceneevent.md)
  An event that a credential session sends to a UIKit scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsessionwindowscenedelegate)*