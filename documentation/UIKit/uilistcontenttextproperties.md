# UIListContentTextProperties

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

Properties that affect the list content configuration’s text.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@interface UIListContentTextProperties : NSObject
```

## Topics

### Configuring text properties
- [font](./uilistcontenttextproperties/font.md)
  The font for the text.
- [color](./uilistcontenttextproperties/color.md)
  The color of the text.
- [colorTransformer](./uilistcontenttextproperties/colortransformer.md)
  The color transformer for resolving the text color.
- [- resolvedColor](./uilistcontenttextproperties/resolvedcolor.md)
  Generates the resolved color for the specified color, using the text color and color transformer.
- [alignment](./uilistcontenttextproperties/alignment.md)
  The alignment for the text.
- [lineBreakMode](./uilistcontenttextproperties/linebreakmode.md)
  The line break mode to use for the text.
- [numberOfLines](./uilistcontenttextproperties/numberoflines.md)
  The maximum number of lines for the text.
- [adjustsFontSizeToFitWidth](./uilistcontenttextproperties/adjustsfontsizetofitwidth.md)
  A Boolean value that determines whether the configuration automatically adjusts the font size of the text when necessary to fit in the available width.
- [minimumScaleFactor](./uilistcontenttextproperties/minimumscalefactor.md)
  The smallest multiplier for the font size that the configuration uses to make the text fit.
- [allowsDefaultTighteningForTruncation](./uilistcontenttextproperties/allowsdefaulttighteningfortruncation.md)
  A Boolean value that determines whether the configuration tightens the text before truncating.
- [adjustsFontForContentSizeCategory](./uilistcontenttextproperties/adjustsfontforcontentsizecategory.md)
  A Boolean value that determines whether the configuration automatically updates the font when the content size category changes.
- [UIListContentTextAlignment](./uilistcontenttextalignment.md)
  Constants that specify the visual alignment of the text.
- [transform](./uilistcontenttextproperties/transform.md)
  The transform to apply to the text.
- [UIListContentTextTransform](./uilistcontenttexttransform.md)
  Constants that specify the transform to apply to the text.
- [showsExpansionTextWhenTruncated](./uilistcontenttextproperties/showsexpansiontextwhentruncated.md)
  A Boolean value that determines whether the full text displays when the pointer hovers over the truncated text.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Customizing appearance
- [imageProperties](./uilistcontentconfiguration-c.class/imageproperties.md)
  Properties for configuring the image.
- [textProperties](./uilistcontentconfiguration-c.class/textproperties.md)
  Properties for configuring the primary text.
- [secondaryTextProperties](./uilistcontentconfiguration-c.class/secondarytextproperties.md)
  Properties for configuring the secondary text.
- [UIListContentImageProperties](./uilistcontentimageproperties.md)
  Properties that affect the list content configuration’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontenttextproperties)*