# prepareToPlay(completionHandler:)

**Framework**: Media Player  
**Kind**: method

Prepares a music player for playback.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func prepareToPlay() async throws
```

#### Discussion

Call this function to ensure that the system buffers the first item in the queue and it’s ready to play. The system executes the code in the completion handler after it buffers the first item in the queue.

## Parameters

- `completionHandler`: A block that the system call after it buffers the first item in the queue and it’s ready to play.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/preparetoplay(completionhandler:))*