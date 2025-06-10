# requestViewController(completionHandler:)

**Framework**: Audio Toolbox  
**Kind**: method

Requests an audio unit’s custom view controller.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+

## Declaration

```swift
func requestViewController() async -> NSViewController?
```

## Mentions

- [Migrating Your Audio Unit Host to the AUv3 API](migrating-your-audio-unit-host-to-the-auv3-api.md)

#### Discussion

The completion handler is called on a thread or dispatch queue internal to the audio unit’s implementation. If the audio unit does not implement a custom view controller, it returns `nil`. If it has a custom view controller, it instantiates the view controller and returns it. The custom view controller must be a subclass of [`AUViewController`](https://developer.apple.com/documentation/CoreAudioKit/AUViewController).


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/requestviewcontroller(completionhandler:))*