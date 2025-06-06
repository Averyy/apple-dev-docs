# displaysPostProcessApplicationControl

**Framework**: Quartz  
**Kind**: property

Specifies whether the post processing application control is displayed.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var displaysPostProcessApplicationControl: Bool { get set }
```

#### Discussion

The post processing application is only relevant when the transfer mode is [`IKScannerDeviceViewTransferMode.fileBased`](ikscannerdeviceviewtransfermode/filebased.md).

## See Also

- [var postProcessApplication: URL!](ikscannerdeviceview/postprocessapplication.md)
  The URL of the application to use for post processing of the scan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikscannerdeviceview/displayspostprocessapplicationcontrol)*