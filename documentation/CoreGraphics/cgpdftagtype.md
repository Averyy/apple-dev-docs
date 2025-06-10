# CGPDFTagType

**Framework**: Core Graphics  
**Kind**: enum

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum CGPDFTagType
```

## Topics

### Enumeration Cases
- [CGPDFTagType.TOC](cgpdftagtype/toc.md)
- [CGPDFTagType.TOCI](cgpdftagtype/toci.md)
- [CGPDFTagType.annotation](cgpdftagtype/annotation.md)
- [CGPDFTagType.art](cgpdftagtype/art.md)
- [CGPDFTagType.bibliography](cgpdftagtype/bibliography.md)
- [CGPDFTagType.blockQuote](cgpdftagtype/blockquote.md)
- [CGPDFTagType.caption](cgpdftagtype/caption.md)
- [CGPDFTagType.code](cgpdftagtype/code.md)
- [CGPDFTagType.div](cgpdftagtype/div.md)
- [CGPDFTagType.document](cgpdftagtype/document.md)
- [CGPDFTagType.figure](cgpdftagtype/figure.md)
- [CGPDFTagType.form](cgpdftagtype/form.md)
- [CGPDFTagType.formula](cgpdftagtype/formula.md)
- [CGPDFTagType.header](cgpdftagtype/header.md)
- [CGPDFTagType.header1](cgpdftagtype/header1.md)
- [CGPDFTagType.header2](cgpdftagtype/header2.md)
- [CGPDFTagType.header3](cgpdftagtype/header3.md)
- [CGPDFTagType.header4](cgpdftagtype/header4.md)
- [CGPDFTagType.header5](cgpdftagtype/header5.md)
- [CGPDFTagType.header6](cgpdftagtype/header6.md)
- [CGPDFTagType.index](cgpdftagtype/index.md)
- [CGPDFTagType.label](cgpdftagtype/label.md)
- [CGPDFTagType.link](cgpdftagtype/link.md)
- [CGPDFTagType.list](cgpdftagtype/list.md)
- [CGPDFTagType.listBody](cgpdftagtype/listbody.md)
- [CGPDFTagType.listItem](cgpdftagtype/listitem.md)
- [CGPDFTagType.nonStructure](cgpdftagtype/nonstructure.md)
- [CGPDFTagType.note](cgpdftagtype/note.md)
- [CGPDFTagType.object](cgpdftagtype/object.md)
- [CGPDFTagType.paragraph](cgpdftagtype/paragraph.md)
- [CGPDFTagType.part](cgpdftagtype/part.md)
- [CGPDFTagType.private](cgpdftagtype/private.md)
- [CGPDFTagType.quote](cgpdftagtype/quote.md)
- [CGPDFTagType.reference](cgpdftagtype/reference.md)
- [CGPDFTagType.ruby](cgpdftagtype/ruby.md)
- [CGPDFTagType.rubyAnnotationText](cgpdftagtype/rubyannotationtext.md)
- [CGPDFTagType.rubyBaseText](cgpdftagtype/rubybasetext.md)
- [CGPDFTagType.rubyPunctuation](cgpdftagtype/rubypunctuation.md)
- [CGPDFTagType.section](cgpdftagtype/section.md)
- [CGPDFTagType.span](cgpdftagtype/span.md)
- [CGPDFTagType.table](cgpdftagtype/table.md)
- [CGPDFTagType.tableBody](cgpdftagtype/tablebody.md)
- [CGPDFTagType.tableDataCell](cgpdftagtype/tabledatacell.md)
- [CGPDFTagType.tableFooter](cgpdftagtype/tablefooter.md)
- [CGPDFTagType.tableHeader](cgpdftagtype/tableheader.md)
- [CGPDFTagType.tableHeaderCell](cgpdftagtype/tableheadercell.md)
- [CGPDFTagType.tableRow](cgpdftagtype/tablerow.md)
- [CGPDFTagType.warichu](cgpdftagtype/warichu.md)
- [CGPDFTagType.warichuPunctiation](cgpdftagtype/warichupunctiation.md)
- [CGPDFTagType.warichuText](cgpdftagtype/warichutext.md)
### Instance Properties
- [var name: UnsafePointer<CChar>](cgpdftagtype/name.md)
### Initializers
- [init?(rawValue: Int32)](cgpdftagtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct CGCaptureOptions](cgcaptureoptions.md)
  Configuration parameters that are used when capturing displays.
- [enum CGColorConversionInfoTransformType](cgcolorconversioninfotransformtype.md)
  Constants describing how a color conversion uses color spaces.
- [enum CGColorRenderingIntent](cgcolorrenderingintent.md)
  Handling options for colors that are not located within the destination color space of a graphics context.
- [struct CGConfigureOption](cgconfigureoption.md)
  The scope of the changes in a display configuration transaction.
- [struct CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags.md)
  The configuration parameters that are passed to a display reconfiguration callback function.
- [enum CGDisplayStreamFrameStatus](cgdisplaystreamframestatus.md)
  Describes a frame update event.
- [enum CGDisplayStreamUpdateRectType](cgdisplaystreamupdaterecttype.md)
  Use these constants to determine which rectangles your app is interested in.
- [enum CGError](cgerror.md)
  A uniform type for result codes returned by functions in Core Graphics.
- [enum CGEventField](cgeventfield.md)
  Constants used as keys to access specialized fields in low-level events.
- [struct CGEventFilterMask](cgeventfiltermask.md)
  Specify masks for classes of low-level events that can be filtered during event suppression states.
- [struct CGEventFlags](cgeventflags.md)
  Constants that indicate the modifier key state at the time an event is created, as well as other event-related states.
- [enum CGEventMouseSubtype](cgeventmousesubtype.md)
  Constants used with the [`CGEventField.mouseEventSubtype`](cgeventfield/mouseeventsubtype.md) event field.
- [enum CGEventSourceStateID](cgeventsourcestateid.md)
  Constants that specify the possible source states of an event source.
- [enum CGEventSuppressionState](cgeventsuppressionstate.md)
  Specify the event suppression states that can occur after posting an event.
- [enum CGEventTapLocation](cgeventtaplocation.md)
  Constants that specify possible tapping points for events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpdftagtype)*