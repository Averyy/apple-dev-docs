# limitedUserInterfaces

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A bitmask of the interface restrictions that currently apply to your app.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var limitedUserInterfaces: CPLimitableUserInterface { get }
```

```objc
@property (nonatomic, readonly) CPLimitableUserInterface limitedUserInterfaces;
```

## Discussion

Use this property to determine which interface features are unavailable or limited. A vehicle might limit interface features for safety reasons or to support vehicle constraints. For example, a vehicle might prevent an app from displaying a keyboard while the vehicle is in motion. The following example shows how to check for the available features from a delegate method:

**Swift**:

```swift
func sessionConfiguration(_ sessionConfiguration: CPSessionConfiguration,
                                           limitedUserInterfacesChanged limitedUserInterfaces: CPLimitableUserInterface) {
    let hasKeyboard = limitedUserInterfaces.contains(.keyboard)
    // Do something with the value.
}
```

**Objective-C**:

```objc
- (void)sessionConfiguration:(CPSessionConfiguration *)sessionConfiguration limitedUserInterfacesChanged:(CPLimitableUserInterface)limitedUserInterfaces {
    Boolean hasKeyboard = limitedUserInterfaces & CPLimitableUserInterfaceKeyboard;
    // Do something with the value.
}
```

## See Also

### Getting the configuration details
- [var contentStyle: CPContentStyle](./contentstyle.md)
  The preferred interface style for your app’s content.
- [var supportsVideoPlayback: Bool](./supportsvideoplayback.md)
  A Boolean value that indicates whether CarPlay supports playing video content.
- [struct CPContentStyle](../cpcontentstyle.md)
  The types of content style that the vehicle allows.
- [struct CPLimitableUserInterface](../cplimitableuserinterface.md)
  The types of interfaces to which a vehicle can limit access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsessionconfiguration/limiteduserinterfaces)*