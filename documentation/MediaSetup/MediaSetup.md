# Media Setup

**Framework**: Media Setup  
**Kind**: module

Enable users to configure HomePod speakers to stream music directly from your media service.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 15.4+
- visionOS 1.0+

#### Overview

Use the Media Setup framework in your iOS app to help users transfer account credentials to their HomePod speakers. For example, if you have an iOS app that already supports Siri media intents to stream music, adopt this framework so the user can set up their HomePod to stream music directly from your media service. Provide endpoints the HomePod speaker can access by adopting [`SiriKit Cloud Media`](https://developer.apple.com/documentation/SiriKitCloudMedia) on your media service.

An [`MSSetupSession`](mssetupsession.md) uses the window you provide in [`presentationAnchor()`](msauthenticationpresentationcontext/presentationanchor().md) to present a configuration view to the user. After the user confirms the configuration, the session assembles a token request from its [`account`](mssetupsession/account.md) and sends it to your OAuth service. When your OAuth service responds with a token, the session verifies the token and [`configurationURL`](msserviceaccount/configurationurl.md). Then it sends that token to the HomePod speakers associated with the user’s Apple ID in the Home app.

For details about applying for the SiriKit Media Intents on HomePod program, see the HomePod section of [`Siri for Developers`](https://developer.apple.comhttps://developer.apple.com/siri).

## Topics

### HomePod Configuration
- [class MSSetupSession](mssetupsession.md)
  An object that manages the transfer of configuration information between your app, the system, your media service, and HomePod speakers.
- [class MSServiceAccount](msserviceaccount.md)
  Account details for accessing a streaming media service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/MediaSetup)*