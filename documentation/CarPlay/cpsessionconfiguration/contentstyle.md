# contentStyle

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The preferred interface style for your app’s content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var contentStyle: CPContentStyle { get }
```

```objc
@property (nonatomic, readonly) CPContentStyle contentStyle;
```

## Discussion

The value in this property tells you whether to render your app using a light or dark style. A vehicle might set the value in this property based on ambient light levels and update the value as the levels change.

## See Also

### Getting the configuration details
- [var limitedUserInterfaces: CPLimitableUserInterface](./limiteduserinterfaces.md)
  A bitmask of the interface restrictions that currently apply to your app.
- [var supportsVideoPlayback: Bool](./supportsvideoplayback.md)
  A Boolean value that indicates whether CarPlay supports playing video content.
- [struct CPContentStyle](../cpcontentstyle.md)
  The types of content style that the vehicle allows.
- [struct CPLimitableUserInterface](../cplimitableuserinterface.md)
  The types of interfaces to which a vehicle can limit access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsessionconfiguration/contentstyle)*