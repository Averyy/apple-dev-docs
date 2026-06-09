# scheduleBuffer(_:atTime:options:completionCallbackType:completionHandler:)

**Framework**: AVFAudio  
**Kind**: method

Schedules playing samples from a read-only audio buffer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func scheduleBuffer(_ buffer: AVReadOnlyAudioPCMBuffer, atTime when: AVAudioTime? = nil, options: AVAudioPlayerNodeBufferOptions = [], completionCallbackType callbackType: AVAudioPlayerNodeCompletionCallbackType = .dataConsumed, completionHandler: (@Sendable () -> Void)? = nil)
```

## Parameters

- `buffer`: The read-only buffer to play.
- `when`: The time at which to play the buffer. Nil means “follow previous command”.
- `options`: Options for looping, interrupting, etc.
- `callbackType`: Specifies when the completion handler is called.
- `completionHandler`: Called after the buffer has been consumed, rendered, or played back. May be nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernode/schedulebuffer(_:attime:options:completioncallbacktype:completionhandler:)-81qje)*