# audiogramSampleType()

**Framework**: HealthKit  
**Kind**: method

Returns an audiogram sample type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func audiogramSampleType() -> HKAudiogramSampleType
```

#### Return Value

The shared [`HKAudiogramSampleType`](hkaudiogramsampletype.md) instance.

#### Discussion

This method returns an instance of the [`HKAudiogramSampleType`](hkaudiogramsampletype.md) concrete subclass. HealthKit uses this type to store and read audiogram data from the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkobjecttype/audiogramsampletype())*