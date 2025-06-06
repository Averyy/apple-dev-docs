# NSPrintInfo

**Framework**: AppKit  
**Kind**: class

An object that stores information that’s used to generate printed output.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSPrintInfo
```

#### Overview

A shared [`NSPrintInfo`](nsprintinfo.md) object is automatically created for an app and is used by default for all printing jobs for that app. The printing information in an [`NSPrintInfo`](nsprintinfo.md) object is stored in a dictionary. To access the standard attributes in the dictionary directly, this class defines a set of keys and provides the [`dictionary()`](nsprintinfo/dictionary().md) method. You can also initialize an instance of this class using the [`init(dictionary:)`](nsprintinfo/init(dictionary:).md) method.

You can use this dictionary to store custom information associated with a print job. Any non-object values should be stored as [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) or [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) objects in the dictionary. See [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) for a list of types which should be stored as numbers. For other non-object values, use the [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) class.

To store custom information that belongs in printing presets you should use the dictionary returned by the [`printSettings`](nsprintinfo/printsettings.md) method.

## Topics

### Creating the Printing Information Object
- [class var shared: NSPrintInfo](nsprintinfo/shared.md)
  The shared printing information object.
- [init(dictionary: [NSPrintInfo.AttributeKey : Any])](nsprintinfo/init(dictionary:).md)
  Returns a printing information object initialized with the parameters in the specified dictionary.
- [convenience init()](nsprintinfo/init.md)
  Creates a printing information object.
- [init(coder: NSCoder)](nsprintinfo/init(coder:).md)
  Creates a printing information object from data in an unarchiver.
### Managing the Printing Rectangle
- [var paperSize: NSSize](nsprintinfo/papersize.md)
  The size of the paper.
- [var topMargin: CGFloat](nsprintinfo/topmargin.md)
  The top margin to the specified size.
- [var bottomMargin: CGFloat](nsprintinfo/bottommargin.md)
  The height of the bottom margin.
- [var leftMargin: CGFloat](nsprintinfo/leftmargin.md)
  The width of the left margin.
- [var rightMargin: CGFloat](nsprintinfo/rightmargin.md)
  The width of the right margin.
- [var imageablePageBounds: NSRect](nsprintinfo/imageablepagebounds.md)
  The imageable area of a sheet of paper specified by the print info.
- [var orientation: NSPrintInfo.PaperOrientation](nsprintinfo/orientation-swift.property.md)
  The orientation attribute.
- [NSPrintInfo.PaperOrientation](nsprintinfo/paperorientation.md)
  Constants that describe the orientation of printing on a page.
- [var paperName: NSPrinter.PaperName?](nsprintinfo/papername.md)
  The name of the currently selected paper size.
- [NSPrinter.PaperName](nsprinter/papername.md)
  The type you use to specify the name of a type of paper.
- [var localizedPaperName: String?](nsprintinfo/localizedpapername.md)
  The human-readable name of the currently selected paper size, suitable for presentation in user interfaces.
### Pagination
- [var horizontalPagination: NSPrintInfo.PaginationMode](nsprintinfo/horizontalpagination.md)
  The horizontal pagination mode.
- [var verticalPagination: NSPrintInfo.PaginationMode](nsprintinfo/verticalpagination.md)
  The vertical pagination to the specified mode.
- [NSPrintInfo.PaginationMode](nsprintinfo/paginationmode.md)
  Constants that specify the different ways in which an image is divided into pages.
### Positioning the Image on the Page
- [var isHorizontallyCentered: Bool](nsprintinfo/ishorizontallycentered.md)
  A Boolean value that indicates whether the image is centered horizontally.
- [var isVerticallyCentered: Bool](nsprintinfo/isverticallycentered.md)
  A Boolean value that indicates whether the image is centered vertically.
### Specifying the Printer
- [var printer: NSPrinter](nsprintinfo/printer.md)
  The printer object to be used for printing.
- [class NSPrinter](nsprinter.md)
  An object that describes a printer’s capabilities.
### Controlling Printing
- [var jobDisposition: NSPrintInfo.JobDisposition](nsprintinfo/jobdisposition-swift.property.md)
  The action specified for the job.
- [NSPrintInfo.JobDisposition](nsprintinfo/jobdisposition-swift.struct.md)
  Constants that specify values for the print job disposition.
- [func setUpPrintOperationDefaultValues()](nsprintinfo/setupprintoperationdefaultvalues.md)
  Validates the attributes encapsulated by the print info.
### Accessing the Print Info Dictionary
- [func dictionary() -> NSMutableDictionary](nsprintinfo/dictionary.md)
  Returns the print info’s dictionary that contains the printing attributes.
### Print Settings Convenience Methods
- [var isSelectionOnly: Bool](nsprintinfo/isselectiononly.md)
  A Boolean value that indicates whether only the currently selected contents should be printed.
- [var scalingFactor: CGFloat](nsprintinfo/scalingfactor.md)
  The current scaling factor.
### Accessing Core Printing Information
- [var printSettings: NSMutableDictionary](nsprintinfo/printsettings.md)
  A mutable dictionary containing the print settings from Core Printing.
- [NSPrintInfo.SettingKey](nsprintinfo/settingkey.md)
  The type you use to specify a print info setting key.
- [func pmPrintSession() -> UnsafeMutableRawPointer](nsprintinfo/pmprintsession.md)
  Returns a Core Printing object configured with the print info’s session information.
- [func pmPageFormat() -> UnsafeMutableRawPointer](nsprintinfo/pmpageformat.md)
  Returns a Core Printing object configured with the print info’s page format information.
- [func pmPrintSettings() -> UnsafeMutableRawPointer](nsprintinfo/pmprintsettings.md)
  Returns a Core Printing object configured with the print info’s print settings information
- [func updateFromPMPageFormat()](nsprintinfo/updatefrompmpageformat.md)
  Synchronizes the print info’s page format information with information from its associated page format object.
- [func updateFromPMPrintSettings()](nsprintinfo/updatefrompmprintsettings.md)
  Synchronizes the print info’s print settings information with information from its associated print settings object.
- [func takeSettings(from: NSPDFInfo)](nsprintinfo/takesettings(from:).md)
  Updates the print info with all the settings and attributes in the specified PDF info object.
### Constants
- [NSPrintInfo.AttributeKey](nsprintinfo/attributekey.md)
  Constants that specify print job attributes.
### Deprecated
- [class var defaultPrinter: NSPrinter?](nsprintinfo/defaultprinter.md)
  Deprecated.
- [NSPrintInfo.Orientation](nsprintinfo/orientation-swift.enum.md)
  Constants that specify page orientations.
- [Deprecated Printing Keys](deprecated-printing-keys.md)
  These keys refer to older printing properties that are no longer used.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSPrinter](nsprinter.md)
  An object that describes a printer’s capabilities.
- [class NSPrintOperation](nsprintoperation.md)
  An object that controls operations that generate Encapsulated PostScript (EPS) code, Portable Document Format (PDF) code, or print jobs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo)*