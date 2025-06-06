# Data providers

**Framework**: ClockKit

Feed data to a complication template.

## Topics

### Text providers
- [class CLKSimpleTextProvider](clksimpletextprovider.md)
  A single line of text to display in your complication interface.
- [class CLKDateTextProvider](clkdatetextprovider.md)
  A formatted string that conveys a date without any time information.
- [class CLKRelativeDateTextProvider](clkrelativedatetextprovider.md)
  A formatted string that conveys the difference in time between the current date and a date that you specify.
- [class CLKTimeIntervalTextProvider](clktimeintervaltextprovider.md)
  A formatted time range.
- [class CLKTimeTextProvider](clktimetextprovider.md)
  A formatted time value.
- [class CLKTextProvider](clktextprovider.md)
  The common behavior for displaying text-based data in a complication.
### Image providers
- [class CLKImageProvider](clkimageprovider.md)
  An image displayed by a complication.
- [class CLKFullColorImageProvider](clkfullcolorimageprovider.md)
  A full-color image displayed by a complication.
### Gauge providers
- [class CLKSimpleGaugeProvider](clksimplegaugeprovider.md)
  A gauge that shows a fractional value.
- [class CLKTimeIntervalGaugeProvider](clktimeintervalgaugeprovider.md)
  A gauge that tracks time intervals.
- [class CLKGaugeProvider](clkgaugeprovider.md)
  An abstract superclass that provides all the common behaviors for the gauge providers.
- [let CLKSimpleGaugeProviderFillFractionEmpty: Float](clksimplegaugeproviderfillfractionempty.md)
  A fill value indicating an empty gauge.
- [enum CLKGaugeProviderStyle](clkgaugeproviderstyle.md)
  Visual styles available for gauges.

## See Also

- [SwiftUI templates](swiftui-templates.md)
  Design complication templates using SwiftUI views.
- [enum ComplicationRenderingMode](complicationrenderingmode.md)
  The complication’s appearance, as specified by the watch face.
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
- [class CLKComplicationTemplate](clkcomplicationtemplate.md)
  An abstract class that defines the base behavior for all templates.
- [enum CLKComplicationFamily](clkcomplicationfamily.md)
  Constants indicating the template groups.
- [CLKComplicationSupportedFamilies](../BundleResources/Information-Property-List/CLKComplicationSupportedFamilies.md)
  The complication families for which the app can provide data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/data-providers)*