# postProcessApplication

**Framework**: Quartz  
**Kind**: property  
**Role**: Instance Property

The URL of the application to use for post processing of the scan.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var postProcessApplication: URL! { get set }
```

```objc
@property (retain) NSURL * postProcessApplication;
```

## Discussion

The post processing application is only relevant when the transfer mode is [`IKScannerDeviceViewTransferMode.fileBased`](../ikscannerdeviceviewtransfermode/filebased.md).

## See Also

### Specifying a Post Processing Application
- [var displaysPostProcessApplicationControl: Bool](./displayspostprocessapplicationcontrol.md)
  Specifies whether the post processing application control is displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikscannerdeviceview/postprocessapplication)*