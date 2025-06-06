# CSActionIdentifier

**Framework**: Core Spotlight  
**Kind**: var

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

#### Discussion

When the user selects a custom action on an indexed item, the system launches your app and invokes [`application(_:continue:restorationHandler:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:continue:restorationHandler:)). The `userInfo` dictionary of the specified [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) includes the corresponding `Info.plist` using this key.

## See Also

- [var actionIdentifiers: [String]](cssearchableitemattributeset/actionidentifiers.md)
  The identifiers that specify custom actions the app supports for the item.
- [var supportsNavigation: NSNumber?](cssearchableitemattributeset/supportsnavigation.md)
  A value that indicates whether the item contains information sufficient to provide navigation to the location it represents.
- [var supportsPhoneCall: NSNumber?](cssearchableitemattributeset/supportsphonecall.md)
  A value that indicates whether the item contains information sufficient to allow a phone call to a number associated with the item.
- [var sharedItemContentType: UTType?](cssearchableitemattributeset/shareditemcontenttype.md)
  The file type of the item to enable the user to share items from Spotlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csactionidentifier)*