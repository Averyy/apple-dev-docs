# CSActionIdentifier

**Framework**: Core Spotlight  
**Kind**: var  
**Role**: Global Variable

A key that specifies the action’s identifier in a user activity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
let CSActionIdentifier: String
```

```c
extern NSString * const CSActionIdentifier;
```

## Discussion

When the user selects a custom action on an indexed item, the system launches your app and invokes [`application(_:continue:restorationHandler:)`](../UIKit/uiapplicationdelegate/application%28_,continue,restorationhandler%29.md). The `userInfo` dictionary of the specified [`NSUserActivity`](../Foundation/nsuseractivity.md) includes the corresponding `Info.plist` using this key.

## See Also

### Describing supporting actions
- [var actionIdentifiers: [String]](./cssearchableitemattributeset/actionidentifiers.md)
  The identifiers that specify custom actions the app supports for the item.
- [var supportsNavigation: NSNumber?](./cssearchableitemattributeset/supportsnavigation.md)
  A value that indicates whether the item contains information sufficient to provide navigation to the location it represents.
- [var supportsPhoneCall: NSNumber?](./cssearchableitemattributeset/supportsphonecall.md)
  A value that indicates whether the item contains information sufficient to allow a phone call to a number associated with the item.
- [var sharedItemContentType: UTType?](./cssearchableitemattributeset/shareditemcontenttype.md)
  The file type of the item to enable the user to share items from Spotlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csactionidentifier)*