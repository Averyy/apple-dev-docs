# NSPrinter

**Framework**: AppKit  
**Kind**: class

An object that describes a printer’s capabilities.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSPrinter
```

#### Overview

[`NSPrinter`](nsprinter.md) provides information about a printer; it does not modify printer attributes or control a printing job. A printer object can be constructed by specifying either the printer name or the make and model of an available printer. Typically, Cocoa apps don’t create [`NSPrinter`](nsprinter.md) objects; instead, the printing system uses these objects to support the printing jobs and when it shows users a list of printers.

## Topics

### Creating the Printer Object
- [init?(name: String)](nsprinter/init(name:).md)
  Creates and returns a printer object initialized with the specified printer name.
- [init?(type: NSPrinter.TypeName)](nsprinter/init(type:).md)
  Creates and returns a printer object initialized to the first available printer with the specified make and model information.
### Getting General Printer Information
- [class var printerNames: [String]](nsprinter/printernames.md)
  Returns the names of all available printers.
- [class var printerTypes: [NSPrinter.TypeName]](nsprinter/printertypes.md)
  Returns descriptions of the makes and models of all available printers.
- [NSPrinter.TypeName](nsprinter/typename.md)
  The type you use to describe a printer’s make and model.
### Getting Attributes
- [var name: String](nsprinter/name.md)
  The printer’s name.
- [var type: NSPrinter.TypeName](nsprinter/type.md)
  A description of the printer’s make and model.
### Getting Page and Printer Information
- [func pageSize(forPaper: NSPrinter.PaperName) -> NSSize](nsprinter/pagesize(forpaper:).md)
  Returns the size of the page for the specified paper type.
- [NSPrinter.PaperName](nsprinter/papername.md)
  The type you use to specify the name of a type of paper.
- [var languageLevel: Int](nsprinter/languagelevel.md)
  The PostScript language level recognized by the printer.
### Querying Tables
- [var deviceDescription: [NSDeviceDescriptionKey : Any]](nsprinter/devicedescription.md)
  A dictionary of keys and values that describe the device.
### Deprecated
- [NSPrinter.TableStatus](nsprinter/tablestatus.md)
  Constants that describe the state of a printer information table stored by a printer object.

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

- [class NSPrintInfo](nsprintinfo.md)
  An object that stores information that’s used to generate printed output.
- [class NSPrintOperation](nsprintoperation.md)
  An object that controls operations that generate Encapsulated PostScript (EPS) code, Portable Document Format (PDF) code, or print jobs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprinter)*