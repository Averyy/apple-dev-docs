# compassSetting

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A value that indicates whether to show compass information as part of your content.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var compassSetting: CPInstrumentClusterSetting { get }
```

```objc
@property (nonatomic, readonly) CPInstrumentClusterSetting compassSetting;
```

## Discussion

Use the value in this property to determine when to include compass heading information with the rest of your app’s content. For information about how to interpret the individual setting values, see the [`CPInstrumentClusterSetting`](../cpinstrumentclustersetting.md) type.

## See Also

### Configuring your instrument cluster interface
- [var instrumentClusterWindow: UIWindow?](./instrumentclusterwindow.md)
  The window you use to display your instrument cluster interface.
- [var inactiveDescriptionVariants: [String]](./inactivedescriptionvariants.md)
  Strings for the vehicle to display in the instrument cluster when navigation isn’t active for your app.
- [var attributedInactiveDescriptionVariants: [NSAttributedString]](./attributedinactivedescriptionvariants.md)
  Attributed strings for the vehicle to display in the instrument cluster when navigation isn’t active for your app.
- [var speedLimitSetting: CPInstrumentClusterSetting](./speedlimitsetting.md)
  A value that indicates whether to show speed limit information as part of your content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinstrumentclustercontroller/compasssetting)*