# Managing Audio with SiriKit

**Framework**: SiriKit

Control audio playback and handle requests to add media using SiriKit Media Intents.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Xcode 16.0+

#### Overview

> **Note**: This sample code project is associated with WWDC 2020 session [`Expand Your SiriKit Media Intents to More Platforms`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2020/10061/).

##### Configure the Sample Code Project

Before you run the sample code project in Xcode:

1. Create an App Group for `com.example.apple-samplecode.ControlAudio.Shared` in your developer portal.
2. Create an App ID for `com.example.apple-samplecode.ControlAudio` in your developer portal and enable it for App Groups, specifying the group you created in the previous step. Additionally, enable SiriKit.
3. Create a Music ID for `music.com.example.apple-samplecode.ControlAudio` in your developer portal.
4. Create a Key for the MusicKit service and create a developer token. For more information on this process, see [`Generating Developer Tokens`](https://developer.apple.com/documentation/AppleMusicAPI/generating-developer-tokens).
5. Copy the developer token to the `developerToken` variable in the `AppleMusicAPIController.swift` file.
6. Create a provisioning profile for `com.example.apple-samplecode.ControlAudio` and `com.example.apple-samplecode.ControlAudio.ControlAudioExtension` in your developer portal.
7. Associate the provisioning profiles with the project in Xcode signing settings.

## See Also

- [Adding Shortcuts for Wind Down](adding-shortcuts-for-wind-down.md)
  Reveal your app’s shortcuts inside the Health app.
- [Booking Rides with SiriKit](booking-rides-with-sirikit.md)
  Add Intents extensions to your app to handle requests to book rides using Siri and Maps.
- [Handling Payment Requests with SiriKit](handling-payment-requests-with-sirikit.md)
  Add an Intent Extension to your app to handle money transfer requests with Siri.
- [Handling Workout Requests with SiriKit](handling-workout-requests-with-sirikit.md)
  Add an Intent Extension to your app that handles requests to control workouts with Siri.
- [Integrating Your App with Siri Event Suggestions](integrating-your-app-with-siri-event-suggestions.md)
  Donate reservations and provide quick access to event details throughout the system.
- [Providing Hands-Free App Control with Intents](providing-hands-free-app-control-with-intents.md)
  Resolve, confirm, and handle intents without an extension.
- [Soup Chef: Accelerating App Interactions with Shortcuts](soup-chef-accelerating-app-interactions-with-shortcuts.md)
  Make it easy for people to use Siri with your app by providing shortcuts to your app’s actions.
- [Soup Chef with App Intents: Migrating custom intents](soup-chef-with-app-intents-migrating-custom-intents.md)
  Integrating App Intents to provide your appʼs actions to Siri and Shortcuts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikit/managing-audio-with-sirikit)*