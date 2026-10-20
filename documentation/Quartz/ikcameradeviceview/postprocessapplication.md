# postProcessApplication

**Framework**: Quartz  
**Kind**: property  
**Role**: Instance Property

The URL of the application used to post process the image.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var postProcessApplication: URL! { get set }
```

```objc
@property (retain) NSURL * postProcessApplication;
```

#### Discussion

The post process application is only relevant when the [`transferMode`](./transfermode.md) is set to [`IKCameraDeviceViewTransferMode.fileBased`](../ikcameradeviceviewtransfermode/filebased.md).

## See Also

### Getting and Setting the Post Processing Application
- [var displaysPostProcessApplicationControl: Bool](./displayspostprocessapplicationcontrol.md)
  Displays whether the post process application control should be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikcameradeviceview/postprocessapplication)*