# alwaysAvailable

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the group is always available through the UI.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var alwaysAvailable: Bool { get set }
```

```objc
@property (nonatomic, assign, readwrite) BOOL alwaysAvailable;
```

## Discussion

Set this property to [`true`](../../Swift/true.md) to ensure that the functionality in this group is available to people regardless of the customization of the groups.

When the value is [`true`](../../Swift/true.md), UIKit places the items in this group in the overflow menu for the [`UIUserInterfaceIdiom.phone`](../uiuserinterfaceidiom/phone.md) and [`UIUserInterfaceIdiom.pad`](../uiuserinterfaceidiom/pad.md) idioms. This property doesn’t have an effect for the [`UIUserInterfaceIdiom.mac`](../uiuserinterfaceidiom/mac.md) idiom.

## See Also

### Configuring the group
- [var barButtonItems: [UIBarButtonItem]](./barbuttonitems.md)
  The bar button items to display on the bar.
- [var representativeItem: UIBarButtonItem?](./representativeitem.md)
  The item to display for a group when space is constrained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/alwaysavailable)*