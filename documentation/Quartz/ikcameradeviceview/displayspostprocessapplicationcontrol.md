# displaysPostProcessApplicationControl

**Framework**: Quartz  
**Kind**: property  
**Role**: Instance Property

Displays whether the post process application control should be displayed.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var displaysPostProcessApplicationControl: Bool { get set }
```

```objc
@property BOOL displaysPostProcessApplicationControl;
```

#### Discussion

The post process application is only relevant when the [`transferMode`](./transfermode.md) is set to [`IKCameraDeviceViewTransferMode.fileBased`](../ikcameradeviceviewtransfermode/filebased.md).

## See Also

### Getting and Setting the Post Processing Application
- [var postProcessApplication: URL!](./postprocessapplication.md)
  The URL of the application used to post process the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikcameradeviceview/displayspostprocessapplicationcontrol)*