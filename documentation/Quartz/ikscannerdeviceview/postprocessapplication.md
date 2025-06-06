# postProcessApplication

**Framework**: Quartz  
**Kind**: property

The URL of the application to use for post processing of the scan.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var postProcessApplication: URL! { get set }
```

#### Discussion

The post processing application is only relevant when the transfer mode is [`IKScannerDeviceViewTransferMode.fileBased`](ikscannerdeviceviewtransfermode/filebased.md).

## See Also

- [var displaysPostProcessApplicationControl: Bool](ikscannerdeviceview/displayspostprocessapplicationcontrol.md)
  Specifies whether the post processing application control is displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikscannerdeviceview/postprocessapplication)*