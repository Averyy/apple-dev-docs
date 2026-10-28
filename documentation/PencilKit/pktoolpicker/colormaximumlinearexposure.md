# colorMaximumLinearExposure

**Framework**: PencilKit  
**Kind**: property  
**Role**: Instance Property

Maximum linear exposure for the color picker used by the tool picker. Can be used to enable picking HDR colors.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
var colorMaximumLinearExposure: CGFloat { get set }
```

```objc
@property (nonatomic, assign) CGFloat colorMaximumLinearExposure;
```

## Discussion

Default value is 1.0 which means only SDR colors can be picked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpicker/colormaximumlinearexposure)*