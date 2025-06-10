# intendedSpatialExperience

**Framework**: Swift  
**Kind**: property

The AudioQueue’s intended spatial audio experience.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
var intendedSpatialExperience: any SpatialAudioExperience { get set }
```

#### Discussion

This value is only useful for output AudioQueues not configured in offline mode; otherwise it’s a no-op.

If unspecified, the property value defaults to `AutomaticSpatialAudio`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/opaquepointer/intendedspatialexperience)*