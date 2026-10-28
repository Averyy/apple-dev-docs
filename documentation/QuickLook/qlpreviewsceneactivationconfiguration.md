# QLPreviewSceneActivationConfiguration

**Framework**: Quick Look  
**Kind**: class  
**Role**: Class

A scene configuration to preview items at the specified URLs.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
class QLPreviewSceneActivationConfiguration
```

```objc
@interface QLPreviewSceneActivationConfiguration : UIWindowSceneActivationConfiguration
```

## Overview

This class provides the configuration for a prominent scene presentation of a preview, either from a swipe gesture or a menu action. The user can detach the prominent Quick Look window and display it independently.

To provide a preview from a swipe gesture, use an instance of this class with [`UIWindowScene.ActivationInteraction`](../UIKit/uiwindowscene/activationinteraction.md). To provide a preview from a menu action, use an instance of this class with [`UIWindowScene.ActivationAction`](../UIKit/uiwindowscene/activationaction.md).

## Topics

### Creating a preview scene activation configuration
- [init(itemsAt: [URL], options: QLPreviewSceneActivationConfiguration.Options?)](./qlpreviewsceneactivationconfiguration/init%28itemsat,options%29.md)
  Creates a preview scene configuration.
### Configuring a preview scene activation
- [QLPreviewSceneActivationConfiguration.Options](./qlpreviewsceneactivationconfiguration/options.md)
  A class that represents the configuration for a preview scene activation.
### Initializers
- [init(itemsAtURLs: [URL], options: QLPreviewSceneActivationConfiguration.Options?)](./qlpreviewsceneactivationconfiguration/init%28itemsaturls,options%29.md)

## Relationships

### Inherits From
- [UIWindowScene.ActivationConfiguration](../UIKit/uiwindowscene/activationconfiguration.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Previews
- [class QLPreviewController](./qlpreviewcontroller.md)
  A specialized view controller for previewing an item.
- [protocol QLPreviewItem](../QuickLookUI/qlpreviewitem.md)
  A protocol that defines a set of properties you implement to make a preview of your app’s content.
- [Previews or thumbnail images for macOS 10.14 or earlier](./previews-or-thumbnail-images-for-macos-10-14-or-earlier.md)
  Create thumbnail images or previews of common files and custom file types in earlier versions of macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewsceneactivationconfiguration)*