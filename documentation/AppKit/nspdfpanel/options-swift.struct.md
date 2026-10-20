# NSPDFPanel.Options

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants used to configure the contents of a PDF panel.

**Availability**:
- macOS 10.9+

## Declaration

```swift
struct Options
```

```c
enum NSPDFPanelOptions : NSInteger;
```

## Topics

### Constants
- [static var showsPaperSize: NSPDFPanel.Options](./options-swift.struct/showspapersize.md)
  The PDF panel shows a menu of paper sizes.
- [static var showsOrientation: NSPDFPanel.Options](./options-swift.struct/showsorientation.md)
  The PDF panel shows the current orientation of the PDF contents, such as landscape or portrait.
- [static var requestsParentDirectory: NSPDFPanel.Options](./options-swift.struct/requestsparentdirectory.md)
  The PDF panel doesn’t show a name field; instead, it allows the user to identify a directory in which to save multiple PDF files. If you set this flag, you’re responsible for appending a filename and the “pdf” extension to the resulting  URL value in the [`NSPDFInfo`](../nspdfinfo.md) object before proceeding with the creation of the PDF file (or calling the `takeSettingsFromPDFInfo` method of [`NSPrintInfo`](../nsprintinfo.md)).
### Initializers
- [init(rawValue: Int)](./options-swift.struct/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspdfpanel/options-swift.struct)*