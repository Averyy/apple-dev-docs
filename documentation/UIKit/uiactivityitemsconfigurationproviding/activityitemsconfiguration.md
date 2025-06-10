# activityItemsConfiguration

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

An object or value that specifies items to share.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
var activityItemsConfiguration: (any UIActivityItemsConfigurationReading)? { get }
```

#### Discussion

To offer a configuration for sharing through Siri or the toolbar in an app built with Mac Catalyst, override this property on the root view controller or a modal view controller. To provide a configuration when your app is displaying a [`UISplitViewController`](uisplitviewcontroller.md), implement this property on the detail view controller.

To offer a configuration for sharing through a context menu, override this property on your [`UIView`](uiview.md) subclass, and attach a [`UIContextMenuInteraction`](uicontextmenuinteraction.md) to that view.

> **Note**:  When the user asks Siri to “share this” on iOS, if both [`activityItemsConfiguration`](uiactivityitemsconfigurationproviding/activityitemsconfiguration.md) and [`activityItemsConfigurationSource`](uiwindowscene/activityitemsconfigurationsource.md) are `nil`, the system uses the [`webpageURL`](https://developer.apple.com/documentation/Foundation/NSUserActivity/webpageURL) property on your app’s current [`userActivity`](uiresponder/useractivity.md) to create shareable content. The system doesn’t offer this fallback behavior in an app built with Mac Catalyst.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityitemsconfigurationproviding/activityitemsconfiguration)*