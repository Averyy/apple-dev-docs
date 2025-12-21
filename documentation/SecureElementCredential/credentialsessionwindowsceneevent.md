# CredentialSessionWindowSceneEvent

**Framework**: SecureElementCredential  
**Kind**: enum

An event that a credential session sends to a UIKit scene.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
enum CredentialSessionWindowSceneEvent
```

## Mentions

- [Accessing and using secure element credentials](accessing-and-using-secure-element-credentials.md)

## Topics

### Events
- [CredentialSessionWindowSceneEvent.presentation](credentialsessionwindowsceneevent/presentation.md)
  The user performs a gesture, such as double-pressing the side button, to present an NFC display.
- [CredentialSessionWindowSceneEvent.readerDetected](credentialsessionwindowsceneevent/readerdetected.md)
  The eligible device detects the RF field of an NFC reader.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [func windowScene(UIWindowScene, didReceiveCredentialSessionWindowSceneEvent: CredentialSessionWindowSceneEvent)](credentialsessionwindowscenedelegate/windowscene(_:didreceivecredentialsessionwindowsceneevent:).md)
  Informs your app that a credential session event initiated a UIKit scene creation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsessionwindowsceneevent)*