# exposureRectOfInterest

**Framework**: AVFoundation  
**Kind**: property

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
var exposureRectOfInterest: CGRect { get set }
```

#### Discussion

Indicates current exposure rectangle of interest of the receiver, if it has one.

The value of this property is a CGRect that determines the receiver’s exposure rectangle of interest, if it has one. It is used as an alternative to -setExposurePointOfInterest:, as it allows for both a location and size to be specified. A value of CGRectMake(0, 0, 1, 1) indicates that the receiver should use the entire field of view when determining the exposure, while CGRectMake(0, 0, 0.25, 0.25) would indicate the top left sixteenth, and CGRectMake(0.75, 0.75, 0.25, 0.25) would indicate the bottom right sixteenth. -setExposureRectOfInterest: throws an NSInvalidArgumentException if isExposureRectOfInterestSupported returns NO. -setExposureRectOfInterest: throws an NSInvalidArgumentException if the size of the provided rectangle is smaller than that returned by minExposureRectOfInterestSize. -setExposureRectOfInterest: throws an NSGenericException if called without first obtaining exclusive access to the receiver using lockForConfiguration:. -setExposureRectOfInterest: will update the receiver’s exposurePointOfInterest to be the center of the rectangle of interest. If the client later sets the receiver’s exposurePointOfInterest, the exposureRectOfInterest will reset to the default rectangle of interest for the new exposure point of interest. If the client changes the activeFormat, the point of interest and rectangle of interest will revert to their default values. Clients can observe automatic changes to the receiver’s exposureRectOfInterest by key value observing this property. Note that setting exposureRectOfInterest alone does not initiate an exposure operation. After setting exposureRectOfInterest, call -setExposureMode: to apply the new rectangle of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/exposurerectofinterest)*