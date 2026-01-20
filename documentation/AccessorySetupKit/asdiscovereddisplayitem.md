# ASDiscoveredDisplayItem

**Framework**: AccessorySetupKit  
**Kind**: class

A picker display item created from customizing a discovered accessory.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+

## Declaration

```swift
class ASDiscoveredDisplayItem
```

## Mentions

- [Discovering and configuring accessories](discovering-and-configuring-accessories.md)

#### Overview

Use this type when your app’s picker uses the [`filterDiscoveryResults`](aspickerdisplaysettings/options-swift.struct/filterdiscoveryresults.md) option. With this option enabled, your discovery session receives [`ASAccessoryEventType.accessoryDiscovered`](asaccessoryeventtype/accessorydiscovered.md) events with discovered accessories. To include a discovered accessory in the picker, create an instance of this class, optionally using the Bluetooth properties of the event’s [`ASDiscoveredAccessory`](asdiscoveredaccessory.md) to provide a more specific name or product image. Then send the `ASDiscoveredDisplayItem` to the picker with the session’s [`updatePicker(showing:completionHandler:)`](asaccessorysession/updatepicker(showing:completionhandler:).md) method.

## Topics

### Creating an updated display item
- [init(name: String, productImage: UIImage, accessory: ASDiscoveredAccessory)](asdiscovereddisplayitem/init(name:productimage:accessory:).md)
  Creates a discovered picker display item with a name and image to display and a descriptor to match discovered accessories.

## Relationships

### Inherits From
- [ASPickerDisplayItem](aspickerdisplayitem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class ASPickerDisplayItem](aspickerdisplayitem.md)
  An accessory as presented by the discovery picker.
- [class ASMigrationDisplayItem](asmigrationdisplayitem.md)
  A previously-discovered accessory as presented by the discovery picker, for use when migrating it to AccessorySetupKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asdiscovereddisplayitem)*