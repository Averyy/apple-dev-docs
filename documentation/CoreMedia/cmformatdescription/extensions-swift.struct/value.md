# CMFormatDescription.Extensions.Value

**Framework**: Core Media  
**Kind**: struct

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct Value
```

## Topics

### Extension Values
- [static func alphaChannelMode(CMFormatDescription.Extensions.Value.AlphaChannelMode) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/alphachannelmode(_:).md)
- [static func chromaLocation(CMFormatDescription.Extensions.Value.ChromaLocation) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/chromalocation(_:).md)
- [static func cleanAperture(width: (numerator: Int, denominator: Int), height: (numerator: Int, denominator: Int), horizontalOffet: (numerator: Int, denominator: Int), verticalOffset: (numerator: Int, denominator: Int)) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/cleanaperture(width:height:horizontaloffet:verticaloffset:)-4b52p.md)
- [static func cleanAperture<Width, Height, Horizontal, Vertical>(width: Width, height: Height, horizontalOffet: Horizontal, verticalOffset: Vertical) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/cleanaperture(width:height:horizontaloffet:verticaloffset:)-2r4iq.md)
- [static func colorPrimaries(CMFormatDescription.Extensions.Value.ColorPrimaries) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/colorprimaries(_:).md)
- [static func data(CFData) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/data(_:).md)
- [static func fieldDetail(CMFormatDescription.Extensions.Value.FieldDetail) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/fielddetail(_:).md)
- [static func fontTable([Int : String]) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/fonttable(_:).md)
- [static func mobile3GPPTextColor(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/mobile3gpptextcolor(red:green:blue:alpha:).md)
- [static func mobile3GPPTextDefaultStyle(startChar: Int, endChar: Int, localFontID: Int, fontFace: CMFormatDescription.Extensions.Value.FontFace, fontSize: Int, foregroundColor: CMFormatDescription.Extensions.Value) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/mobile3gpptextdefaultstyle(startchar:endchar:localfontid:fontface:fontsize:foregroundcolor:).md)
- [static func mpeg2VideoProfile(CMFormatDescription.Extensions.Value.MPEG2VideoProfile) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/mpeg2videoprofile(_:).md)
- [static func number<T>(T) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/number(_:).md)
- [static func pixelAspectRatio<Horizontal, Vertical>(horizontalSpacing: Horizontal, verticalSpacing: Vertical) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/pixelaspectratio(horizontalspacing:verticalspacing:).md)
- [static func qtTextColor(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/qttextcolor(red:green:blue:alpha:).md)
- [static func qtTextDefaultStyle(startChar: Int, height: Int, ascent: Int, localFontID: Int, fontFace: CMFormatDescription.Extensions.Value.FontFace, fontSize: Int, foregroundColor: CMFormatDescription.Extensions.Value, defaultFontName: String?) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/qttextdefaultstyle(startchar:height:ascent:localfontid:fontface:fontsize:foregroundcolor:defaultfontname:).md)
- [static func sourceReferenceName(value: String, langCode: Int) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/sourcereferencename(value:langcode:).md)
- [static func string(String) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/string(_:)-52jj4.md)
- [static func string(CFString) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/string(_:)-6y3ip.md)
- [static func textDisplayFlags(Set<CMFormatDescription.Extensions.Value.TextDisplayFlags>) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/textdisplayflags(_:).md)
- [static func textJustification(CMFormatDescription.Extensions.Value.TextJustification) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/textjustification(_:).md)
- [static func textRect(top: Int, left: Int, bottom: Int, right: Int) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/textrect(top:left:bottom:right:).md)
- [static func transferFunction(CMFormatDescription.Extensions.Value.TransferFunction) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/transferfunction(_:).md)
- [static func vendor(CMFormatDescription.Extensions.Value.Vendor) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/vendor(_:)-1uvag.md)
- [static func vendor(String) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/vendor(_:)-5y6sw.md)
- [static func yCbCrMatrix(CMFormatDescription.Extensions.Value.YCbCrMatrix) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/ycbcrmatrix(_:).md)
### Inspecting Extension Values
- [var propertyListRepresentation: CFPropertyList](cmformatdescription/extensions-swift.struct/value/propertylistrepresentation.md)
### Comparing Extension Values
- [static func == (CMFormatDescription, CMFormatDescription) -> Bool](cmformatdescription/==(_:_:).md)
  Equality is derived from
### Creating Extension Values
- [init(CFPropertyList)](cmformatdescription/extensions-swift.struct/value/init(_:).md)
### Constants
- [CMFormatDescription.Extensions.Value.AlphaChannelMode](cmformatdescription/extensions-swift.struct/value/alphachannelmode.md)
- [CMFormatDescription.Extensions.Value.ChromaLocation](cmformatdescription/extensions-swift.struct/value/chromalocation.md)
- [CMFormatDescription.Extensions.Value.ColorPrimaries](cmformatdescription/extensions-swift.struct/value/colorprimaries.md)
- [CMFormatDescription.Extensions.Value.FieldDetail](cmformatdescription/extensions-swift.struct/value/fielddetail.md)
- [CMFormatDescription.Extensions.Value.FontFace](cmformatdescription/extensions-swift.struct/value/fontface.md)
- [CMFormatDescription.Extensions.Value.MPEG2VideoProfile](cmformatdescription/extensions-swift.struct/value/mpeg2videoprofile.md)
- [CMFormatDescription.Extensions.Value.TextDisplayFlags](cmformatdescription/extensions-swift.struct/value/textdisplayflags.md)
- [CMFormatDescription.Extensions.Value.TextJustification](cmformatdescription/extensions-swift.struct/value/textjustification.md)
- [CMFormatDescription.Extensions.Value.TransferFunction](cmformatdescription/extensions-swift.struct/value/transferfunction.md)
- [CMFormatDescription.Extensions.Value.Vendor](cmformatdescription/extensions-swift.struct/value/vendor.md)
- [CMFormatDescription.Extensions.Value.YCbCrMatrix](cmformatdescription/extensions-swift.struct/value/ycbcrmatrix.md)
### Structures
- [CMFormatDescription.Extensions.Value.ContentColorVolume](cmformatdescription/extensions-swift.struct/value/contentcolorvolume.md)
- [CMFormatDescription.Extensions.Value.HeroEye](cmformatdescription/extensions-swift.struct/value/heroeye.md)
- [CMFormatDescription.Extensions.Value.LogTransferFunction](cmformatdescription/extensions-swift.struct/value/logtransferfunction.md)
- [CMFormatDescription.Extensions.Value.ProjectionKind](cmformatdescription/extensions-swift.struct/value/projectionkind.md)
- [CMFormatDescription.Extensions.Value.ViewPackingKind](cmformatdescription/extensions-swift.struct/value/viewpackingkind.md)
### Type Methods
- [static func cameraCalibrationDataLensCollection(CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/cameracalibrationdatalenscollection(_:).md)
- [static func heroEye(CMFormatDescription.Extensions.Value.HeroEye) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/heroeye(_:).md)
- [static func logTransferFunction(CMFormatDescription.Extensions.Value.LogTransferFunction) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/logtransferfunction(_:).md)
- [static func projectionKind(CMFormatDescription.Extensions.Value.ProjectionKind) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/projectionkind(_:).md)
- [static func viewPackingKind(CMFormatDescription.Extensions.Value.ViewPackingKind) -> CMFormatDescription.Extensions.Value](cmformatdescription/extensions-swift.struct/value/viewpackingkind(_:).md)
### Enumerations
- [CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection](cmformatdescription/extensions-swift.struct/value/cameracalibrationdatalenscollection.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [CMFormatDescription.Extensions.Key](cmformatdescription/extensions-swift.struct/key.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription/extensions-swift.struct/value)*