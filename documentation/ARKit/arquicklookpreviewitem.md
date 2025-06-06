# ARQuickLookPreviewItem

**Framework**: ARKit  
**Kind**: class

An object for customizing the AR Quick Look experience.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARQuickLookPreviewItem
```

## Mentions

- [Previewing a Model with AR Quick Look](previewing-a-model-with-ar-quick-look.md)

#### Overview

Use this class when you want to control the background, designate which content the share sheet shares, or disable scaling in case it’s not appropriate to allow the user to scale a particular model.

## Topics

### Creating a Preview Item
- [init(fileAt: URL)](arquicklookpreviewitem/init(fileat:).md)
  Initializes a new AR Quick Look preview item.
### Scaling Content
- [var allowsContentScaling: Bool](arquicklookpreviewitem/allowscontentscaling.md)
  A Boolean value that determines whether the user can scale your virtual content using pinch gestures.
### Interacting with Content
- [var canonicalWebPageURL: URL?](arquicklookpreviewitem/canonicalwebpageurl.md)
  The web URL to share when the user invokes the share sheet.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [QLPreviewItem](../QuickLookUI/QLPreviewItem.md)

## See Also

- [Previewing a Model with AR Quick Look](previewing-a-model-with-ar-quick-look.md)
  Display a model or scene that the user can move, scale, and share with others.
- [Adding Visual Effects in AR Quick Look and RealityKit](adding-visual-effects-in-ar-quick-look-and-realitykit.md)
  Balance the appearance and performance of your AR experiences with modeling strategies.
- [Adding an Apple Pay Button or a Custom Action in AR Quick Look](adding-an-apple-pay-button-or-a-custom-action-in-ar-quick-look.md)
  Provide a banner that users can tap to make a purchase or perform a custom action in an AR experience.
- [USDZ schemas for AR](../RealityKit/usdz-schemas-for-ar.md)
  Add augmented reality functionality to your 3D content using USDZ schemas.
- [Specifying a lighting environment in AR Quick Look](specifying-a-lighting-environment-in-ar-quick-look.md)
  Add metadata to your USDZ file to specify its lighting characteristics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arquicklookpreviewitem)*