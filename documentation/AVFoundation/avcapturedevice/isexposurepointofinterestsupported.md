# isExposurePointOfInterestSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the device supports a point of interest for exposure.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var isExposurePointOfInterestSupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isExposurePointOfInterestSupported) BOOL exposurePointOfInterestSupported;
```

## Discussion

This property is key-value observable.

## See Also

### Setting an exposure point of interest
- [var exposurePointOfInterest: CGPoint](./exposurepointofinterest.md)
  The point of interest for exposure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isexposurepointofinterestsupported)*