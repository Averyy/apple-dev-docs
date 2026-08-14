# MSSetupSession

**Framework**: Media Setup  
**Kind**: class

An object that manages the transfer of configuration information between your app, the system, your media service, and HomePod speakers.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
class MSSetupSession
```

#### Overview

An `MSSetupSession` object guides the user through connecting HomePod speakers in their home to your media service. When your iOS app calls [`start()`](mssetupsession/start().md), the session displays a setup view in the window you provide in [`presentationAnchor()`](msauthenticationpresentationcontext/presentationanchor().md). The session embeds your app icon and the [`serviceName`](msserviceaccount/servicename.md) you provide into this setup view.

![A wireframe showing the setup view Media Setup displays to the user, with callouts indicating where your app’s icon and your media service’s name appear.](/images/com.apple.mediasetup/media-3729379@2x.png)

After the user confirms the setup by tapping the “Use in Home” button, the system requests an OAuth token from your authentication service and shares the token with HomePod speakers in the user’s home.

## Topics

### Preparing the Configuration View
- [init(serviceAccount: MSServiceAccount)](mssetupsession/init(serviceaccount:).md)
  Creates a new session.
- [var account: MSServiceAccount](mssetupsession/account.md)
  The streaming media service account for the session to configure.
### Presenting the Configuration View
- [var presentationContext: (any MSAuthenticationPresentationContext)?](mssetupsession/presentationcontext.md)
  A delegate that provides media setup display information to the system.
- [protocol MSAuthenticationPresentationContext](msauthenticationpresentationcontext.md)
  A protocol that provides media setup display information to the system.
- [func start() throws](mssetupsession/start.md)
  Initiates the service configuration process and sends the account details of the streaming media service to the user’s HomePod speakers.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class MSServiceAccount](msserviceaccount.md)
  Account details for accessing a streaming media service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediasetup/mssetupsession)*