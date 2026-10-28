# NSTextHighlightStyleAttributeName

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

An attribute that adds a highlight color to the text to emphasize it.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```c
extern NSAttributedStringKey const NSTextHighlightStyleAttributeName;
```

## Overview

The value of this attribute is an [`NSTextHighlightStyle`](./nstexthighlightstyle.md) structure. The default value of this attribute is `nil`, which does not add a highlight to the text.

A highlight adds a background color behind the text, and adjusts the color of the text itself to contrast appropriately. The [`NSTextHighlightStyleDefault`](./nstexthighlightstyledefault.md) highlight style applies the system highlight color to your text. To apply a different color, add the [`NSTextHighlightColorSchemeAttributeName`](./nstexthighlightcolorschemeattributename.md) attribute to your text in addition to this one. Use the [`NSTextHighlightColorSchemeAttributeName`](./nstexthighlightcolorschemeattributename.md) key to specify which highlight color you want.

## See Also

### Getting text attribute keys
- [NSLinkAttributeName](./nslinkattributename.md)
  The link for the text.
- [NSShadowAttributeName](./nsshadowattributename.md)
  The shadow of the text.
- [NSTextEffectAttributeName](./nstexteffectattributename.md)
  An attribute that applies a text effect to the text.
- [NSTextHighlightColorSchemeAttributeName](./nstexthighlightcolorschemeattributename.md)
  The custom highlight color to apply to the text.
- [UITextItemTagAttributeName](./uitextitemtagattributename.md)
  The name of a custom tag associated with a text item.
- [NSWritingToolsExclusionAttributeName](./nswritingtoolsexclusionattributename.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstexthighlightstyleattributename)*