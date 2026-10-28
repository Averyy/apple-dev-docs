# displaysPostProcessApplicationControl

**Framework**: Quartz  
**Kind**: property  
**Role**: Instance Property

Specifies whether the post processing application control is displayed.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var displaysPostProcessApplicationControl: Bool { get set }
```

```objc
@property BOOL displaysPostProcessApplicationControl;
```

## Discussion

The post processing application is only relevant when the transfer mode is [`IKScannerDeviceViewTransferMode.fileBased`](../ikscannerdeviceviewtransfermode/filebased.md).

## See Also

### Specifying a Post Processing Application
- [var postProcessApplication: URL!](./postprocessapplication.md)
  The URL of the application to use for post processing of the scan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikscannerdeviceview/displayspostprocessapplicationcontrol)*