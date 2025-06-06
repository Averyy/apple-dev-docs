# windowScene(_:didReceiveCredentialSessionWindowSceneEvent:)

**Framework**: SecureElementCredential  
**Kind**: method  
**Required**: Yes

Informs your app that a credential session event initiated a UIKit scene creation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
func windowScene(_ windowScene: UIWindowScene, didReceiveCredentialSessionWindowSceneEvent event: CredentialSessionWindowSceneEvent)
```

## Parameters

- `windowScene`: The scene object connected to your app.
- `event`: The   that initiated the new scene.

## See Also

- [enum CredentialSessionWindowSceneEvent](credentialsessionwindowsceneevent.md)
  An event that a credential session sends to a UIKit scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsessionwindowscenedelegate/windowscene(_:didreceivecredentialsessionwindowsceneevent:))*