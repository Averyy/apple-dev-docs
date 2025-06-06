# begin(category:completionHandler:)

**Framework**: AVFAudio  
**Kind**: method

Begins routing arbitration to take ownership of a nearby Bluetooth audio route.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func begin(category: AVAudioRoutingArbiter.Category) async throws -> Bool
```

#### Discussion

Call this method to tell the operating system to arbitrate with nearby Apple devices to take ownership of a supported Bluetooth audio device. When arbitration completes, the system calls the completion handler, passing a Boolean that indicates whether the audio device changed. In either case, begin using audio as normal.

## Parameters

- `category`: A category that describes how the app uses audio.
- `handler`: A completion handler the system calls asynchronously when the system completes audio routing arbitration. This closure takes the following parameters:

## See Also

- [AVAudioRoutingArbiter.Category](avaudioroutingarbiter/category.md)
  Categories that describe the general nature of your app’s audio use.
- [func leave()](avaudioroutingarbiter/leave.md)
  Stops an app’s participation in audio routing arbitration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioroutingarbiter/begin(category:completionhandler:))*