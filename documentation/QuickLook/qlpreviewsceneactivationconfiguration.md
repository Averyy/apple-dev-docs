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

To provide a preview from a swipe gesture, use an instance of this class with [`UIWindowScene.ActivationInteraction`](https://developer.apple.com/documentation/uikit/uiwindowscene/activationinteraction). To provide a preview from a menu action, use an instance of this class with [`UIWindowScene.ActivationAction`](https://developer.apple.com/documentation/uikit/uiwindowscene/activationaction).

## Topics

### Creating a preview scene activation configuration
- [init(itemsAt: [URL], options: QLPreviewSceneActivationConfiguration.Options?)](qlpreviewsceneactivationconfiguration/init(itemsat:options:).md)
  Creates a preview scene configuration.
### Configuring a preview scene activation
- [QLPreviewSceneActivationConfiguration.Options](qlpreviewsceneactivationconfiguration/options.md)
  A class that represents the configuration for a preview scene activation.
### Initializers
- [init(itemsAtURLs: [URL], options: QLPreviewSceneActivationConfiguration.Options?)](qlpreviewsceneactivationconfiguration/init(itemsaturls:options:).md)

## Relationships

### Inherits From
- [UIWindowScene.ActivationConfiguration](../uikit/uiwindowscene/activationconfiguration.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class QLPreviewController](qlpreviewcontroller.md)
  A specialized view controller for previewing an item.
- [protocol QLPreviewItem](../quicklookui/qlpreviewitem.md)
  A protocol that defines a set of properties you implement to make a preview of your application’s content.
- [Previews or thumbnail images for macOS 10.14 or earlier](previews-or-thumbnail-images-for-macos-10-14-or-earlier.md)
  Create thumbnail images or previews of common files and custom file types in earlier versions of macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewsceneactivationconfiguration)*