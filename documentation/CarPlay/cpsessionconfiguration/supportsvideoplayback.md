# supportsVideoPlayback

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether CarPlay supports playing video content.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
var supportsVideoPlayback: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL supportsVideoPlayback;
```

## Discussion

Use this property to determine when to enable your app’s video playback interface. The value of this property doesn’t change while your app runs. If a vehicle supports video playback, that support remains available throughout the current session. However, the system might disable the rendering of video content to ensure the safe operation of the vehicle. For example, the vehicle might play only the audio portion of a video while it’s in motion.

## See Also

### Getting the configuration details
- [var contentStyle: CPContentStyle](./contentstyle.md)
  The preferred interface style for your app’s content.
- [var limitedUserInterfaces: CPLimitableUserInterface](./limiteduserinterfaces.md)
  A bitmask of the interface restrictions that currently apply to your app.
- [struct CPContentStyle](../cpcontentstyle.md)
  The types of content style that the vehicle allows.
- [struct CPLimitableUserInterface](../cplimitableuserinterface.md)
  The types of interfaces to which a vehicle can limit access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsessionconfiguration/supportsvideoplayback)*