# focusRectOfInterest

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
var focusRectOfInterest: CGRect { get set }
```

#### Discussion

Indicates current focus rectangle of interest of the receiver, if it has one.

The value of this property is a CGRect that determines the receiver’s focus rectangle of interest, if it has one. It is used as an alternative to -setFocusPointOfInterest:, as it allows for both a location and size to be specified. A value of CGRectMake(0, 0, 1, 1) indicates that the receiver should use the entire field of view when determining the focus, while CGRectMake(0, 0, 0.25, 0.25) would indicate the top left sixteenth, and CGRectMake(0.75, 0.75, 0.25, 0.25) would indicate the bottom right sixteenth. -setFocusRectOfInterest: throws an NSInvalidArgumentException if isFocusRectOfInterestSupported returns NO. -setFocusRectOfInterest: throws an NSInvalidArgumentException if the size of the provided rectangle is smaller than that returned by minFocusRectOfInterestSize. -setFocusRectOfInterest: throws an NSGenericException if called without first obtaining exclusive access to the receiver using lockForConfiguration:. -setFocusRectOfInterest: will update the receiver’s focusPointOfInterest to be the center of the rectangle of interest. If the client later sets the receiver’s focusPointOfInterest, the focusRectOfInterest will reset to the default rectangle of interest for the new focus point of interest. If the client changes the activeFormat, the point of interest and rectangle of interest will revert to their default values. Clients can observe automatic changes to the receiver’s focusRectOfInterest by key value observing this property. Note that setting focusRectOfInterest alone does not initiate a focus operation. After setting focusRectOfInterest, call -setFocusMode: to apply the new rectangle of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/focusrectofinterest)*