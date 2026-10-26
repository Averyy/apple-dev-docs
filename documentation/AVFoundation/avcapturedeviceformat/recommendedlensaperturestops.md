# recommendedLensApertureStops

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A sorted array of recommended values for the [`lensAperture`](../avcapturedevice/lensaperture.md) property.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- tvOS 27.0+

## Declaration

```objc
@property (nonatomic, readonly) NSArray<NSNumber *> * recommendedLensApertureStops;
```

#### Discussion

If this array contains a single item, the aperture is fixed at that value and cannot be changed. If this array contains multiple items, the first will be the minimum recommended 𝑓-stop and the last will be the maximum recommended 𝑓-stop.

Using values from this list may provide optimal calibration and lens characteristics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceformat/recommendedlensaperturestops)*