# exposureTargetOffset

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The metered exposure level’s offset from the target exposure value, in exposure value (EV) units.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var exposureTargetOffset: Float { get }
```

```objc
@property (nonatomic, readonly) float exposureTargetOffset;
```

#### Discussion

The value of property indicates the difference between the metered exposure level of the current scene and the target exposure value.

This property is key-value observable.

## See Also

### Adjusting exposure compensation
- [var exposureTargetBias: Float](./exposuretargetbias.md)
  The bias to apply to the target exposure value, in exposure value (EV) units.
- [var minExposureTargetBias: Float](./minexposuretargetbias.md)
  The minimum supported exposure bias, in exposure value (EV) units.
- [var maxExposureTargetBias: Float](./maxexposuretargetbias.md)
  The maximum supported exposure bias, in exposure value (EV) units.
- [class let currentExposureTargetBias: Float](./currentexposuretargetbias.md)
  A special constant that represents the current exposure bias value.
- [func setExposureTargetBias(Float, completionHandler: ((CMTime) -> Void)?)](./setexposuretargetbias%28_,completionhandler%29.md)
  Sets the bias to apply to the target exposure value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/exposuretargetoffset)*