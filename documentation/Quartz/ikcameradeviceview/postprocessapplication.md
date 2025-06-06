# postProcessApplication

**Framework**: Quartz  
**Kind**: property

The URL of the application used to post process the image.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var postProcessApplication: URL! { get set }
```

#### Discussion

The post process application is only relevant when the [`transferMode`](ikcameradeviceview/transfermode.md) is set to [`IKCameraDeviceViewTransferMode.fileBased`](ikcameradeviceviewtransfermode/filebased.md).

## See Also

- [var displaysPostProcessApplicationControl: Bool](ikcameradeviceview/displayspostprocessapplicationcontrol.md)
  Displays whether the post process application control should be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikcameradeviceview/postprocessapplication)*