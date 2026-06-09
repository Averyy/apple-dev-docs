# setDisconnectedFromSystemAudio(_:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Changes whether the player is disconnected from system audio. This method allows you to dynamically change the player’s system audio connection. The operation is asynchronous. Each call to this method will invoke its own completion handler when the operation completes. When changing from `false` to `true`, you should typically call this method first, then deactivate the `AVAudioSession` to allow other audio to resume.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
func setDisconnectedFromSystemAudio(_ disconnected: Bool, completionHandler: (@Sendable () -> Void)? = nil)
```

#### Using the Completion Handler

In a scenario where changing the value from `false` to `true` should also allow other system audio to resume, you should only deactivate the audio session once the player has disconnected from system audio.

```swift
// Disconnect from system audio and let other audio resume
player.setDisconnectedFromSystemAudio(true) {
	try AVAudioSession.sharedInstance().setActive(false, options: .notifyOthersOnDeactivation)
}
```

## Parameters

- `disconnected`: `true` to disconnect from system audio, `false` to connect to it.
- `completionHandler`: A block that is called when the connection state change is complete. This block is called on an arbitrary queue. Defaults to `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/setdisconnectedfromsystemaudio(_:completionhandler:))*