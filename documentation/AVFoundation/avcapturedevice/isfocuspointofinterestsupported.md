# isFocusPointOfInterestSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the device supports a point of interest for focus.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var isFocusPointOfInterestSupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isFocusPointOfInterestSupported) BOOL focusPointOfInterestSupported;
```

#### Discussion

This property is key-value observable.

## See Also

### Setting a focus point of interest
- [var focusPointOfInterest: CGPoint](./focuspointofinterest.md)
  The point of interest for focusing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isfocuspointofinterestsupported)*