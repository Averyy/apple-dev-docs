# actionIdentifiers

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

The identifiers that specify custom actions the app supports for the item.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
var actionIdentifiers: [String] { get set }
```

```objc
@property (copy) NSArray<NSString *> * actionIdentifiers;
```

## Discussion

The identifiers correspond to the [`CoreSpotlightActionIdentifier`](../../BundleResources/information-property-list/corespotlightactions/corespotlightactionidentifier.md) values you specify in the [`CoreSpotlightActions`](../../BundleResources/information-property-list/corespotlightactions.md) key of the app’s `Info.plist` file.

When the user selects a custom action on an indexed item, the system launches your app and invokes [`application(_:continue:restorationHandler:)`](../../UIKit/uiapplicationdelegate/application%28_,continue,restorationhandler%29.md). The `userInfo` dictionary of the specified [`NSUserActivity`](../../Foundation/nsuseractivity.md) includes the corresponding `Info.plist` entry using the key [`CSActionIdentifier`](../csactionidentifier.md).

## See Also

### Describing supporting actions
- [var supportsNavigation: NSNumber?](./supportsnavigation.md)
  A value that indicates whether the item contains information sufficient to provide navigation to the location it represents.
- [var supportsPhoneCall: NSNumber?](./supportsphonecall.md)
  A value that indicates whether the item contains information sufficient to allow a phone call to a number associated with the item.
- [var sharedItemContentType: UTType?](./shareditemcontenttype.md)
  The file type of the item to enable the user to share items from Spotlight.
- [let CSActionIdentifier: String](../csactionidentifier.md)
  A key that specifies the action’s identifier in a user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/actionidentifiers)*