# defaultRectForExposurePoint(ofInterest:)

**Framework**: AVFoundation  
**Kind**: method

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
func defaultRectForExposurePoint(ofInterest pointOfInterest: CGPoint) -> CGRect
```

#### Discussion

Returns the default rectangle of interest that is used for a given exposure point of interest.

Pass (0.5, 0.5) to get the exposure rectangle of interest used for the default exposure point of interest at (0.5, 0.5). This method returns CGRectNull if isExposureRectOfInterestSupported returns NO.

## Parameters

- `pointOfInterest`: Point of interest for which we are returning the default rectangle of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/defaultrectforexposurepoint(ofinterest:))*