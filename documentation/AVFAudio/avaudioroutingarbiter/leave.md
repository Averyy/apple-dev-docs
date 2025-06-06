# leave()

**Framework**: AVFAudio  
**Kind**: method

Stops an app’s participation in audio routing arbitration.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func leave()
```

#### Discussion

Configure your app to notify the system when the app stops using audio for an undetermined duration. For example, for a Voice over IP (VoIP) app, call this method when the VoIP call ends. Calling this method allows the system to make an informed decision when multiple Apple devices are trying to take ownership of a Bluetooth audio route.

## See Also

- [func begin(category: AVAudioRoutingArbiter.Category, completionHandler: (Bool, (any Error)?) -> Void)](avaudioroutingarbiter/begin(category:completionhandler:).md)
  Begins routing arbitration to take ownership of a nearby Bluetooth audio route.
- [AVAudioRoutingArbiter.Category](avaudioroutingarbiter/category.md)
  Categories that describe the general nature of your app’s audio use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioroutingarbiter/leave())*