# displaysPostProcessApplicationControl

**Framework**: Quartz  
**Kind**: property

Displays whether the post process application control should be displayed.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var displaysPostProcessApplicationControl: Bool { get set }
```

#### Discussion

The post process application is only relevant when the [`transferMode`](ikcameradeviceview/transfermode.md) is set to [`IKCameraDeviceViewTransferMode.fileBased`](ikcameradeviceviewtransfermode/filebased.md).

## See Also

- [var postProcessApplication: URL!](ikcameradeviceview/postprocessapplication.md)
  The URL of the application used to post process the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikcameradeviceview/displayspostprocessapplicationcontrol)*