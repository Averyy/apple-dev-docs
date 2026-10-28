# isBackgroundReplacementActive

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether Background Replacement is currently active on a capture device.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
var isBackgroundReplacementActive: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isBackgroundReplacementActive) BOOL backgroundReplacementActive;
```

## Discussion

This property is key-value observable.

## See Also

### Configuring background replacement
- [class var isBackgroundReplacementEnabled: Bool](./isbackgroundreplacementenabled.md)
  A class property that indicates whether a person enables the Background Replacement feature for this app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isbackgroundreplacementactive)*