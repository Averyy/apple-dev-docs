# actionIdentifiers

**Framework**: Core Spotlight  
**Kind**: property

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

#### Discussion

The identifiers correspond to the [`CoreSpotlightActionIdentifier`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CoreSpotlightActions/CoreSpotlightActionIdentifier) values you specify in the [`CoreSpotlightActions`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CoreSpotlightActions) key of the app’s `Info.plist` file.

When the user selects a custom action on an indexed item, the system launches your app and invokes [`application(_:continue:restorationHandler:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:continue:restorationHandler:)). The `userInfo` dictionary of the specified [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) includes the corresponding `Info.plist` entry using the key [`CSActionIdentifier`](csactionidentifier.md).

## See Also

- [var supportsNavigation: NSNumber?](cssearchableitemattributeset/supportsnavigation.md)
  A value that indicates whether the item contains information sufficient to provide navigation to the location it represents.
- [var supportsPhoneCall: NSNumber?](cssearchableitemattributeset/supportsphonecall.md)
  A value that indicates whether the item contains information sufficient to allow a phone call to a number associated with the item.
- [var sharedItemContentType: UTType?](cssearchableitemattributeset/shareditemcontenttype.md)
  The file type of the item to enable the user to share items from Spotlight.
- [let CSActionIdentifier: String](csactionidentifier.md)
  A key that specifies the action’s identifier in a user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/actionidentifiers)*