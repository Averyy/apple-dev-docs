# QLPreviewSceneActivationConfiguration

**Framework**: Quick Look  
**Kind**: class

A scene configuration to preview items at the specified URLs.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
class QLPreviewSceneActivationConfiguration
```

#### Overview

This class provides the configuration for a prominent scene presentation of a preview, either from a swipe gesture or a menu action. The user can detach the prominent Quick Look window and display it independently.

To provide a preview from a swipe gesture, use an instance of this class with [`UIWindowScene.ActivationInteraction`](https://developer.apple.com/documentation/UIKit/UIWindowScene/ActivationInteraction). To provide a preview from a menu action, use an instance of this class with [`UIWindowScene.ActivationAction`](https://developer.apple.com/documentation/UIKit/UIWindowScene/ActivationAction).

## Topics

### Creating a preview scene activation configuration
- [init(itemsAt: [URL], options: QLPreviewSceneActivationConfiguration.Options?)](qlpreviewsceneactivationconfiguration/init(itemsat:options:).md)
  Creates a preview scene configuration.
### Configuring a preview scene activation
- [QLPreviewSceneActivationConfiguration.Options](qlpreviewsceneactivationconfiguration/options.md)
  A class that represents the configuration for a preview scene activation.

## Relationships

### Inherits From
- [UIWindowScene.ActivationConfiguration](../UIKit/UIWindowScene/ActivationConfiguration.md)
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

- [class QLPreviewController](qlpreviewcontroller.md)
  A specialized view controller for previewing an item.
- [protocol QLPreviewItem : NSObjectProtocol](../QuickLookUI/QLPreviewItem.md)
  A protocol that defines a set of properties you implement to make a preview of your application’s content.
- [Previews or thumbnail images for macOS 10.14 or earlier](previews-or-thumbnail-images-for-macos-10-14-or-earlier.md)
  Create thumbnail images or previews of common files and custom file types in earlier versions of macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewsceneactivationconfiguration)*