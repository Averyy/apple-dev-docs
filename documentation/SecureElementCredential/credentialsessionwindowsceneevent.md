# CredentialSessionWindowSceneEvent

**Framework**: SecureElementCredential  
**Kind**: enum

A CredentialSession event send to a `UIScene` or `UIWindowScene`.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
enum CredentialSessionWindowSceneEvent
```

## Mentions

- [Accessing and using secure element credentials](accessing-and-using-secure-element-credentials.md)

#### Overview

All files that refer to symbols defined here should never `import SwiftUI` Importing SwiftUI with UIKit will result in ambiguous symbols during compilation.

## Topics

### Events
- [CredentialSessionWindowSceneEvent.presentation](credentialsessionwindowsceneevent/presentation.md)
  User has perform gesture on device to request for app presentation
- [CredentialSessionWindowSceneEvent.readerDetected](credentialsessionwindowsceneevent/readerdetected.md)
  External NFC reader is detected, i.e. presence of a NFC field

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [func windowScene(UIWindowScene, didReceiveCredentialSessionWindowSceneEvent: CredentialSessionWindowSceneEvent)](credentialsessionwindowscenedelegate/windowscene(_:didreceivecredentialsessionwindowsceneevent:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsessionwindowsceneevent)*