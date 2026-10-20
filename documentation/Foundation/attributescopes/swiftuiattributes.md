# AttributeScopes.SwiftUIAttributes

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

Attribute scopes that SwiftUI defines.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct SwiftUIAttributes
```

## Topics

### Using Color Attributes
- [let backgroundColor: AttributeScopes.SwiftUIAttributes.BackgroundColorAttribute](./swiftuiattributes/backgroundcolor.md)
  A property for accessing a background color attribute.
- [let foregroundColor: AttributeScopes.SwiftUIAttributes.ForegroundColorAttribute](./swiftuiattributes/foregroundcolor.md)
  A property for accessing a foreground color attribute.
### Using Font and Layout Attributes
- [let font: AttributeScopes.SwiftUIAttributes.FontAttribute](./swiftuiattributes/font.md)
  A property for accessing a font attribute.
- [let tracking: AttributeScopes.SwiftUIAttributes.TrackingAttribute](./swiftuiattributes/tracking.md)
  A property for accessing a tracking attribute.
### Using Text Styling Attributes
- [let baselineOffset: AttributeScopes.SwiftUIAttributes.BaselineOffsetAttribute](./swiftuiattributes/baselineoffset.md)
  A property for accessing a baseline offset attribute.
- [let kern: AttributeScopes.SwiftUIAttributes.KerningAttribute](./swiftuiattributes/kern.md)
  A property for accessing a kerning attribute.
### Using Foundation Attributes
- [let foundation: AttributeScopes.FoundationAttributes](./swiftuiattributes/foundation.md)
  A property for accessing attributes defined by the Foundation framework.
### Instance Properties
- [let accessibility: AttributeScopes.AccessibilityAttributes](./swiftuiattributes/accessibility.md)
- [let adaptiveImageGlyph: AttributeScopes.SwiftUIAttributes.AdaptiveImageGlyphAttribute](./swiftuiattributes/adaptiveimageglyph.md)
- [let alignment: AttributeScopes.CoreTextAttributes.TextAlignmentAttribute](./swiftuiattributes/alignment.md)
  The horizontal alignment of a paragraph.
- [let lineHeight: AttributeScopes.CoreTextAttributes.LineHeightAttribute](./swiftuiattributes/lineheight.md)
  The line height definition of a paragraph.
- [let strikethroughStyle: AttributeScopes.SwiftUIAttributes.StrikethroughStyleAttribute](./swiftuiattributes/strikethroughstyle.md)
- [let underlineStyle: AttributeScopes.SwiftUIAttributes.UnderlineStyleAttribute](./swiftuiattributes/underlinestyle.md)
### Enumerations
- [AttributeScopes.SwiftUIAttributes.AdaptiveImageGlyphAttribute](./swiftuiattributes/adaptiveimageglyphattribute.md)
  A key for an adaptive image glyph inside a run of attributed text.
- [AttributeScopes.SwiftUIAttributes.BackgroundColorAttribute](./swiftuiattributes/backgroundcolorattribute.md)
  A key for the color that fills the area behind a run of attributed text.
- [AttributeScopes.SwiftUIAttributes.BaselineOffsetAttribute](./swiftuiattributes/baselineoffsetattribute.md)
  A key for the distance a run of attributed text shifts from its baseline.
- [AttributeScopes.SwiftUIAttributes.FontAttribute](./swiftuiattributes/fontattribute.md)
  A key for the font of a run of attributed text.
- [AttributeScopes.SwiftUIAttributes.ForegroundColorAttribute](./swiftuiattributes/foregroundcolorattribute.md)
  A key for the color that draws a run of attributed text.
- [AttributeScopes.SwiftUIAttributes.KerningAttribute](./swiftuiattributes/kerningattribute.md)
  A key for the space added between specific pairs of characters in a run of attributed text.
- [AttributeScopes.SwiftUIAttributes.StrikethroughStyleAttribute](./swiftuiattributes/strikethroughstyleattribute.md)
  A key for the line drawn through a run of attributed text.
- [AttributeScopes.SwiftUIAttributes.TrackingAttribute](./swiftuiattributes/trackingattribute.md)
  A key for the space added between every character of a run of attributed text.
- [AttributeScopes.SwiftUIAttributes.UnderlineStyleAttribute](./swiftuiattributes/underlinestyleattribute.md)
  A key for the line drawn under a run of attributed text.

## Relationships

### Conforms To
- [AttributeScope](../attributescope.md)
- [DecodingConfigurationProviding](../decodingconfigurationproviding.md)
- [EncodingConfigurationProviding](../encodingconfigurationproviding.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### SwiftUI-Defined Attributes
- [var swiftUI: AttributeScopes.SwiftUIAttributes.Type](./swiftui.md)
  A property for accessing the attribute scopes that SwiftUI defines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/swiftuiattributes)*