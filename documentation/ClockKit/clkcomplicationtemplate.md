# CLKComplicationTemplate

**Framework**: ClockKit  
**Kind**: class

An abstract class that defines the base behavior for all templates.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class CLKComplicationTemplate
```

#### Overview

You don’t create instances of this class directly. Instead, you create instances of one of the concrete subclasses and use the resulting object to specify the data for your complication.

## Topics

### Setting the Tint Color
- [var tintColor: UIColor?](clkcomplicationtemplate/tintcolor.md)
  The tint color to apply to elements of the template.
### Displaying Previews
- [func previewContext(faceColor: CLKComplicationTemplate.PreviewFaceColor) -> some View](clkcomplicationtemplate/previewcontext(facecolor:).md)
  Returns a view that Xcode can display as a preview.
- [CLKComplicationTemplate.PreviewFaceColor](clkcomplicationtemplate/previewfacecolor.md)
  The valid face colors for complication templates.
### Specifying Styles
- [enum CLKComplicationColumnAlignment](clkcomplicationcolumnalignment.md)
  Constants indicating the alignment of text in columns.
- [enum CLKComplicationRingStyle](clkcomplicationringstyle.md)
  Constants indicating the appearance of a progress ring.
### Creating Empty Templates
- [init()](clkcomplicationtemplate/init.md)
  Creates a new complication.
- [class func new() -> Self](clkcomplicationtemplate/new.md)
  Returns a new complication.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CLKComplicationTemplateCircularSmallRingImage](clkcomplicationtemplatecircularsmallringimage.md)
- [CLKComplicationTemplateCircularSmallRingText](clkcomplicationtemplatecircularsmallringtext.md)
- [CLKComplicationTemplateCircularSmallSimpleImage](clkcomplicationtemplatecircularsmallsimpleimage.md)
- [CLKComplicationTemplateCircularSmallSimpleText](clkcomplicationtemplatecircularsmallsimpletext.md)
- [CLKComplicationTemplateCircularSmallStackImage](clkcomplicationtemplatecircularsmallstackimage.md)
- [CLKComplicationTemplateCircularSmallStackText](clkcomplicationtemplatecircularsmallstacktext.md)
- [CLKComplicationTemplateExtraLargeColumnsText](clkcomplicationtemplateextralargecolumnstext.md)
- [CLKComplicationTemplateExtraLargeRingImage](clkcomplicationtemplateextralargeringimage.md)
- [CLKComplicationTemplateExtraLargeRingText](clkcomplicationtemplateextralargeringtext.md)
- [CLKComplicationTemplateExtraLargeSimpleImage](clkcomplicationtemplateextralargesimpleimage.md)
- [CLKComplicationTemplateExtraLargeSimpleText](clkcomplicationtemplateextralargesimpletext.md)
- [CLKComplicationTemplateExtraLargeStackImage](clkcomplicationtemplateextralargestackimage.md)
- [CLKComplicationTemplateExtraLargeStackText](clkcomplicationtemplateextralargestacktext.md)
- [CLKComplicationTemplateGraphicBezelCircularText](clkcomplicationtemplategraphicbezelcirculartext.md)
- [CLKComplicationTemplateGraphicCircular](clkcomplicationtemplategraphiccircular.md)
- [CLKComplicationTemplateGraphicCornerCircularImage](clkcomplicationtemplategraphiccornercircularimage.md)
- [CLKComplicationTemplateGraphicCornerCircularView](clkcomplicationtemplategraphiccornercircularview.md)
- [CLKComplicationTemplateGraphicCornerGaugeImage](clkcomplicationtemplategraphiccornergaugeimage.md)
- [CLKComplicationTemplateGraphicCornerGaugeText](clkcomplicationtemplategraphiccornergaugetext.md)
- [CLKComplicationTemplateGraphicCornerGaugeView](clkcomplicationtemplategraphiccornergaugeview.md)
- [CLKComplicationTemplateGraphicCornerStackText](clkcomplicationtemplategraphiccornerstacktext.md)
- [CLKComplicationTemplateGraphicCornerTextImage](clkcomplicationtemplategraphiccornertextimage.md)
- [CLKComplicationTemplateGraphicCornerTextView](clkcomplicationtemplategraphiccornertextview.md)
- [CLKComplicationTemplateGraphicExtraLargeCircular](clkcomplicationtemplategraphicextralargecircular.md)
- [CLKComplicationTemplateGraphicRectangularFullImage](clkcomplicationtemplategraphicrectangularfullimage.md)
- [CLKComplicationTemplateGraphicRectangularFullView](clkcomplicationtemplategraphicrectangularfullview.md)
- [CLKComplicationTemplateGraphicRectangularLargeImage](clkcomplicationtemplategraphicrectangularlargeimage.md)
- [CLKComplicationTemplateGraphicRectangularLargeView](clkcomplicationtemplategraphicrectangularlargeview.md)
- [CLKComplicationTemplateGraphicRectangularStandardBody](clkcomplicationtemplategraphicrectangularstandardbody.md)
- [CLKComplicationTemplateGraphicRectangularStandardBodyView](clkcomplicationtemplategraphicrectangularstandardbodyview.md)
- [CLKComplicationTemplateGraphicRectangularTextGauge](clkcomplicationtemplategraphicrectangulartextgauge.md)
- [CLKComplicationTemplateGraphicRectangularTextGaugeView](clkcomplicationtemplategraphicrectangulartextgaugeview.md)
- [CLKComplicationTemplateModularLargeColumns](clkcomplicationtemplatemodularlargecolumns.md)
- [CLKComplicationTemplateModularLargeStandardBody](clkcomplicationtemplatemodularlargestandardbody.md)
- [CLKComplicationTemplateModularLargeTable](clkcomplicationtemplatemodularlargetable.md)
- [CLKComplicationTemplateModularLargeTallBody](clkcomplicationtemplatemodularlargetallbody.md)
- [CLKComplicationTemplateModularSmallColumnsText](clkcomplicationtemplatemodularsmallcolumnstext.md)
- [CLKComplicationTemplateModularSmallRingImage](clkcomplicationtemplatemodularsmallringimage.md)
- [CLKComplicationTemplateModularSmallRingText](clkcomplicationtemplatemodularsmallringtext.md)
- [CLKComplicationTemplateModularSmallSimpleImage](clkcomplicationtemplatemodularsmallsimpleimage.md)
- [CLKComplicationTemplateModularSmallSimpleText](clkcomplicationtemplatemodularsmallsimpletext.md)
- [CLKComplicationTemplateModularSmallStackImage](clkcomplicationtemplatemodularsmallstackimage.md)
- [CLKComplicationTemplateModularSmallStackText](clkcomplicationtemplatemodularsmallstacktext.md)
- [CLKComplicationTemplateUtilitarianLargeFlat](clkcomplicationtemplateutilitarianlargeflat.md)
- [CLKComplicationTemplateUtilitarianSmallFlat](clkcomplicationtemplateutilitariansmallflat.md)
- [CLKComplicationTemplateUtilitarianSmallRingImage](clkcomplicationtemplateutilitariansmallringimage.md)
- [CLKComplicationTemplateUtilitarianSmallRingText](clkcomplicationtemplateutilitariansmallringtext.md)
- [CLKComplicationTemplateUtilitarianSmallSquare](clkcomplicationtemplateutilitariansmallsquare.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [SwiftUI templates](swiftui-templates.md)
  Design complication templates using SwiftUI views.
- [enum ComplicationRenderingMode](complicationrenderingmode.md)
  The complication’s appearance, as specified by the watch face.
- [Data providers](data-providers.md)
  Feed data to a complication template.
- [Circular small](circular-small.md)
  Display small, circular content in the corners of the Color watch face.
- [Extra large](extra-large.md)
  Display content on the X-Large watch face.
- [Modular small](modular-small.md)
  Display content in the smaller spaces of the Modular watch face.
- [Modular large](modular-large.md)
  Display multiple rows of content in the large, central complication on the Modular watch face.
- [Utilitarian](utilitarian.md)
  Use the utilitarian templates to display content on a variety of watch faces, including the Utility, Chronograph, Simple, and character watch faces.
- [Graphic](graphic.md)
  Display visually rich content on watch faces.
- [enum CLKComplicationFamily](clkcomplicationfamily.md)
  Constants indicating the template groups.
- [CLKComplicationSupportedFamilies](../BundleResources/Information-Property-List/CLKComplicationSupportedFamilies.md)
  The complication families for which the app can provide data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplate)*