# instrumentClusterWindow

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The window you use to display your instrument cluster interface.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var instrumentClusterWindow: UIWindow? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) UIWindow * instrumentClusterWindow;
```

## Discussion

Use the window in this property to configure your instrument cluster interface. Specifically, instantiate a custom view controller your app uses to display content in the instrument cluster and assign it to the window’s [`rootViewController`](../../UIKit/uiwindow/rootviewcontroller.md) property. Maintain a reference to your view controller so you can update its content when the vehicle settings change.

## See Also

### Configuring your instrument cluster interface
- [var inactiveDescriptionVariants: [String]](./inactivedescriptionvariants.md)
  Strings for the vehicle to display in the instrument cluster when navigation isn’t active for your app.
- [var attributedInactiveDescriptionVariants: [NSAttributedString]](./attributedinactivedescriptionvariants.md)
  Attributed strings for the vehicle to display in the instrument cluster when navigation isn’t active for your app.
- [var speedLimitSetting: CPInstrumentClusterSetting](./speedlimitsetting.md)
  A value that indicates whether to show speed limit information as part of your content.
- [var compassSetting: CPInstrumentClusterSetting](./compasssetting.md)
  A value that indicates whether to show compass information as part of your content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinstrumentclustercontroller/instrumentclusterwindow)*