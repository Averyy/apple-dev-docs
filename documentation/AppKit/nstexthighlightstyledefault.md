# NSTextHighlightStyleDefault

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The default highlight style to apply to text.

**Availability**:
- macOS 15.0+

## Declaration

```c
extern NSTextHighlightStyle const NSTextHighlightStyleDefault;
```

## Discussion

Use this constant as the value for the [`NSTextHighlightStyleAttributeName`](./nstexthighlightstyleattributename.md) attribute. The system applies the default highlight color to your text. To specify a different highlight color, add the [`NSTextHighlightColorSchemeAttributeName`](./nstexthighlightcolorschemeattributename.md) attribute to your text and set its value to the color you want.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstexthighlightstyledefault)*