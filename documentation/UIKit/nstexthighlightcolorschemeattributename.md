# NSTextHighlightColorSchemeAttributeName

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

The custom highlight color to apply to the text.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```c
extern NSAttributedStringKey const NSTextHighlightColorSchemeAttributeName;
```

## Overview

The value of this attribute is an [`NSTextHighlightColorScheme`](./nstexthighlightcolorscheme.md) structure. The default value of this attribute is nil, which applies the default system highlight color to the text when the [`NSTextHighlightStyleAttributeName`](./nstexthighlightstyleattributename.md) attribute is present.

A highlight adds a background color behind the text, and applies a contrasting foreground color to the text itself. Set the value of this attribute to [`NSTextHighlightColorSchemeDefault`](./nstexthighlightcolorschemedefault.md), or don’t specify the attribute at all, to apply a highlight with the default system color. Specify a different value for this attribute to apply that highlight color instead.

## See Also

### Getting text attribute keys
- [NSLinkAttributeName](./nslinkattributename.md)
  The link for the text.
- [NSShadowAttributeName](./nsshadowattributename.md)
  The shadow of the text.
- [NSTextEffectAttributeName](./nstexteffectattributename.md)
  An attribute that applies a text effect to the text.
- [NSTextHighlightStyleAttributeName](./nstexthighlightstyleattributename.md)
  An attribute that adds a highlight color to the text to emphasize it.
- [UITextItemTagAttributeName](./uitextitemtagattributename.md)
  The name of a custom tag associated with a text item.
- [NSWritingToolsExclusionAttributeName](./nswritingtoolsexclusionattributename.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstexthighlightcolorschemeattributename)*