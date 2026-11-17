# attributedInactiveDescriptionVariants

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

Attributed strings for the vehicle to display in the instrument cluster when navigation isn’t active for your app.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var attributedInactiveDescriptionVariants: [NSAttributedString] { get set }
```

```objc
@property (nonatomic, copy) NSArray<NSAttributedString *> * attributedInactiveDescriptionVariants;
```

## Discussion

When your app’s navigation isn’t active, configure this property with attributed strings that offer relevant information. For example, you might specify the road on which the person is driving. Provide attributed strings of different lengths and place the more preferred strings at the beginning of the array, followed by the remaining strings. When the vehicle has a place to put your text, it chooses the most preferred attributed string in the array that also fits the available space.

When creating your attributed strings, the only supported attribute is the [`attachment`](../../Foundation/nsattributedstring/key/attachment.md) attribute. Use this attribute to annotate the string with images. The maximum allowed size for images is 64x25 points. CarPlay removes all other attributes from your attributed string.

When setting a value, this property makes a copy of the string you provide. If the vehicle supports styled text, the system prefers the values in this property over the values in the [`inactiveDescriptionVariants`](./inactivedescriptionvariants.md) property.

## See Also

### Configuring your instrument cluster interface
- [var instrumentClusterWindow: UIWindow?](./instrumentclusterwindow.md)
  The window you use to display your instrument cluster interface.
- [var inactiveDescriptionVariants: [String]](./inactivedescriptionvariants.md)
  Strings for the vehicle to display in the instrument cluster when navigation isn’t active for your app.
- [var speedLimitSetting: CPInstrumentClusterSetting](./speedlimitsetting.md)
  A value that indicates whether to show speed limit information as part of your content.
- [var compassSetting: CPInstrumentClusterSetting](./compasssetting.md)
  A value that indicates whether to show compass information as part of your content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinstrumentclustercontroller/attributedinactivedescriptionvariants)*