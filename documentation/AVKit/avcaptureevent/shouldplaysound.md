# shouldPlaySound

**Framework**: AVKit  
**Kind**: property

Indicates whether a sound must be played manually using the `playSound` method.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
var shouldPlaySound: Bool { get }
```

#### Discussion

This property is `YES` only when both of the following conditions are true:

1. The event was triggered by an AirPod stem click.
2. The default capture sound is disabled.

If `shouldPlaySound ` is `NO`, calling `playSound` will have no effect. Omitting the sound when expected can significantly impact the user experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureevent/shouldplaysound)*