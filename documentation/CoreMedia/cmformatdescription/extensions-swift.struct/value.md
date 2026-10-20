# CMFormatDescription.Extensions.Value

**Framework**: Core Media  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
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
- [static func alphaChannelMode(CMFormatDescription.Extensions.Value.AlphaChannelMode) -> CMFormatDescription.Extensions.Value](./value/alphachannelmode%28_%29.md)
- [static func chromaLocation(CMFormatDescription.Extensions.Value.ChromaLocation) -> CMFormatDescription.Extensions.Value](./value/chromalocation%28_%29.md)
- [static func cleanAperture(width: (numerator: Int, denominator: Int), height: (numerator: Int, denominator: Int), horizontalOffet: (numerator: Int, denominator: Int), verticalOffset: (numerator: Int, denominator: Int)) -> CMFormatDescription.Extensions.Value](./value/cleanaperture%28width,height,horizontaloffet,verticaloffset%29-4b52p.md)
- [static func cleanAperture<Width, Height, Horizontal, Vertical>(width: Width, height: Height, horizontalOffet: Horizontal, verticalOffset: Vertical) -> CMFormatDescription.Extensions.Value](./value/cleanaperture%28width,height,horizontaloffet,verticaloffset%29-2r4iq.md)
- [static func colorPrimaries(CMFormatDescription.Extensions.Value.ColorPrimaries) -> CMFormatDescription.Extensions.Value](./value/colorprimaries%28_%29.md)
- [static func data(CFData) -> CMFormatDescription.Extensions.Value](./value/data%28_%29.md)
- [static func fieldDetail(CMFormatDescription.Extensions.Value.FieldDetail) -> CMFormatDescription.Extensions.Value](./value/fielddetail%28_%29.md)
- [static func fontTable([Int : String]) -> CMFormatDescription.Extensions.Value](./value/fonttable%28_%29.md)
- [static func mobile3GPPTextColor(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat) -> CMFormatDescription.Extensions.Value](./value/mobile3gpptextcolor%28red,green,blue,alpha%29.md)
- [static func mobile3GPPTextDefaultStyle(startChar: Int, endChar: Int, localFontID: Int, fontFace: CMFormatDescription.Extensions.Value.FontFace, fontSize: Int, foregroundColor: CMFormatDescription.Extensions.Value) -> CMFormatDescription.Extensions.Value](./value/mobile3gpptextdefaultstyle%28startchar,endchar,localfontid,fontface,fontsize,foregroundcolor%29.md)
- [static func mpeg2VideoProfile(CMFormatDescription.Extensions.Value.MPEG2VideoProfile) -> CMFormatDescription.Extensions.Value](./value/mpeg2videoprofile%28_%29.md)
- [static func number<T>(T) -> CMFormatDescription.Extensions.Value](./value/number%28_%29.md)
- [static func pixelAspectRatio<Horizontal, Vertical>(horizontalSpacing: Horizontal, verticalSpacing: Vertical) -> CMFormatDescription.Extensions.Value](./value/pixelaspectratio%28horizontalspacing,verticalspacing%29.md)
- [static func qtTextColor(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat) -> CMFormatDescription.Extensions.Value](./value/qttextcolor%28red,green,blue,alpha%29.md)
- [static func qtTextDefaultStyle(startChar: Int, height: Int, ascent: Int, localFontID: Int, fontFace: CMFormatDescription.Extensions.Value.FontFace, fontSize: Int, foregroundColor: CMFormatDescription.Extensions.Value, defaultFontName: String?) -> CMFormatDescription.Extensions.Value](./value/qttextdefaultstyle%28startchar,height,ascent,localfontid,fontface,fontsize,foregroundcolor,defaultfontname%29.md)
- [static func sourceReferenceName(value: String, langCode: Int) -> CMFormatDescription.Extensions.Value](./value/sourcereferencename%28value,langcode%29.md)
- [static func string(String) -> CMFormatDescription.Extensions.Value](./value/string%28_%29-52jj4.md)
- [static func string(CFString) -> CMFormatDescription.Extensions.Value](./value/string%28_%29-6y3ip.md)
- [static func textDisplayFlags(Set<CMFormatDescription.Extensions.Value.TextDisplayFlags>) -> CMFormatDescription.Extensions.Value](./value/textdisplayflags%28_%29.md)
- [static func textJustification(CMFormatDescription.Extensions.Value.TextJustification) -> CMFormatDescription.Extensions.Value](./value/textjustification%28_%29.md)
- [static func textRect(top: Int, left: Int, bottom: Int, right: Int) -> CMFormatDescription.Extensions.Value](./value/textrect%28top,left,bottom,right%29.md)
- [static func transferFunction(CMFormatDescription.Extensions.Value.TransferFunction) -> CMFormatDescription.Extensions.Value](./value/transferfunction%28_%29.md)
- [static func vendor(CMFormatDescription.Extensions.Value.Vendor) -> CMFormatDescription.Extensions.Value](./value/vendor%28_%29-1uvag.md)
- [static func vendor(String) -> CMFormatDescription.Extensions.Value](./value/vendor%28_%29-5y6sw.md)
- [static func yCbCrMatrix(CMFormatDescription.Extensions.Value.YCbCrMatrix) -> CMFormatDescription.Extensions.Value](./value/ycbcrmatrix%28_%29.md)
### Inspecting Extension Values
- [var propertyListRepresentation: CFPropertyList](./value/propertylistrepresentation.md)
### Comparing Extension Values
- [static func == (CMFormatDescription, CMFormatDescription) -> Bool](../eqeq%28_,_%29.md)
  Equality is derived from
### Creating Extension Values
- [init(CFPropertyList)](./value/init%28_%29.md)
### Constants
- [CMFormatDescription.Extensions.Value.AlphaChannelMode](./value/alphachannelmode.md)
- [CMFormatDescription.Extensions.Value.ChromaLocation](./value/chromalocation.md)
- [CMFormatDescription.Extensions.Value.ColorPrimaries](./value/colorprimaries.md)
- [CMFormatDescription.Extensions.Value.FieldDetail](./value/fielddetail.md)
- [CMFormatDescription.Extensions.Value.FontFace](./value/fontface.md)
- [CMFormatDescription.Extensions.Value.MPEG2VideoProfile](./value/mpeg2videoprofile.md)
- [CMFormatDescription.Extensions.Value.TextDisplayFlags](./value/textdisplayflags.md)
- [CMFormatDescription.Extensions.Value.TextJustification](./value/textjustification.md)
- [CMFormatDescription.Extensions.Value.TransferFunction](./value/transferfunction.md)
- [CMFormatDescription.Extensions.Value.Vendor](./value/vendor.md)
- [CMFormatDescription.Extensions.Value.YCbCrMatrix](./value/ycbcrmatrix.md)
### Structures
- [CMFormatDescription.Extensions.Value.ContentColorVolume](./value/contentcolorvolume.md)
- [CMFormatDescription.Extensions.Value.HeroEye](./value/heroeye.md)
- [CMFormatDescription.Extensions.Value.LogTransferFunction](./value/logtransferfunction.md)
- [CMFormatDescription.Extensions.Value.ProjectionKind](./value/projectionkind.md)
- [CMFormatDescription.Extensions.Value.ViewPackingKind](./value/viewpackingkind.md)
### Type Methods
- [static func cameraCalibrationDataLensCollection(CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection) -> CMFormatDescription.Extensions.Value](./value/cameracalibrationdatalenscollection%28_%29.md)
- [static func heroEye(CMFormatDescription.Extensions.Value.HeroEye) -> CMFormatDescription.Extensions.Value](./value/heroeye%28_%29.md)
- [static func logTransferFunction(CMFormatDescription.Extensions.Value.LogTransferFunction) -> CMFormatDescription.Extensions.Value](./value/logtransferfunction%28_%29.md)
- [static func projectionKind(CMFormatDescription.Extensions.Value.ProjectionKind) -> CMFormatDescription.Extensions.Value](./value/projectionkind%28_%29.md)
- [static func viewPackingKind(CMFormatDescription.Extensions.Value.ViewPackingKind) -> CMFormatDescription.Extensions.Value](./value/viewpackingkind%28_%29.md)
### Enumerations
- [CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection](./value/cameracalibrationdatalenscollection.md)

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Constants
- [CMFormatDescription.Extensions.Key](./key.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription/extensions-swift.struct/value)*