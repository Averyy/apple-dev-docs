# INDefaultCardTemplate

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A card template for customizing the Siri watch face for a shortcut.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class INDefaultCardTemplate
```

```objc
@interface INDefaultCardTemplate : NSObject
```

## Mentions

- [Displaying Shortcut Information in a Siri Watch Face Card](../SiriKit/displaying-shortcut-information-in-a-siri-watch-face-card.md)

## Overview

The Siri watch face displays a relevant shortcut using information from the [`INIntent`](./inintent.md) or [`NSUserActivity`](../Foundation/nsuseractivity.md) provided when creating the shortcut. If you want to provide watch specific information—for example, to display a shorter title—provide the relevant shortcut a default card template by setting the [`watchTemplate`](./inrelevantshortcut/watchtemplate.md) property. The template allows your app to set the [`title`](./indefaultcardtemplate/title.md), [`subtitle`](./indefaultcardtemplate/subtitle.md), and [`image`](./indefaultcardtemplate/image.md). For more information, see [Displaying Shortcut Information in a Siri Watch Face Card](../SiriKit/displaying-shortcut-information-in-a-siri-watch-face-card.md).

![A screenshot of the Siri watch face showing a custom default card template with callouts for image, title, and subtitle.](https://developer.apple.com/tutorials/images/com.apple.sirikit/media-3030289@2x.png)

## Topics

### Creating a Default Card Template
- [init(title: String)](./indefaultcardtemplate/init%28title%29.md)
  Creates a default card template with the specified title.
### Managing Template Information
- [var title: String](./indefaultcardtemplate/title.md)
  The title displayed in the Siri watch face card.
- [var subtitle: String?](./indefaultcardtemplate/subtitle.md)
  The subtitle displayed in the Siri watch face card.
- [var image: INImage?](./indefaultcardtemplate/image.md)
  The image displayed in the Siri watch face card.
### Initializers
- [init?(coder: NSCoder)](./indefaultcardtemplate/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Siri watch face
- [Displaying Shortcut Information in a Siri Watch Face Card](../SiriKit/displaying-shortcut-information-in-a-siri-watch-face-card.md)
  Display and customize watch-specific shortcut information with a default card template.
- [Defining Relevant Shortcuts for the Siri Watch Face](../SiriKit/defining-relevant-shortcuts-for-the-siri-watch-face.md)
  Inform Siri when your app’s shortcuts may be useful to the user.
- [class INRelevantShortcut](./inrelevantshortcut.md)
  An object that defines a shortcut and its relevance to the user.
- [class INRelevantShortcutStore](./inrelevantshortcutstore.md)
  An object that saves relevant shortcuts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indefaultcardtemplate)*