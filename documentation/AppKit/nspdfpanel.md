# NSPDFPanel

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A Save or Export as PDF panel that’s consistent with the macOS user interface.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
class NSPDFPanel
```

```objc
@interface NSPDFPanel : NSObject
```

## Overview

A PDF panel has a variety of built-in customization controls, such as page orientation, paper size, and tags. It also supports the use of a custom accessory view controller that allows an app to specify how a PDF file should be created.

## Topics

### Managing the Contents of a PDF Panel
- [var accessoryController: NSViewController?](./nspdfpanel/accessorycontroller.md)
  A view controller for the accessory view that the panel can present.
- [var options: NSPDFPanel.Options](./nspdfpanel/options-swift.property.md)
  A set of configuration options that determine the accessory views the PDF panel should display.
- [var defaultFileName: String](./nspdfpanel/defaultfilename.md)
  The initial value for the user-editable filename shown in the name field of the PDF panel.
### Displaying a PDF Panel
- [func beginSheet(with: NSPDFInfo, modalFor: NSWindow?, completionHandler: (Int) -> Void)](./nspdfpanel/beginsheet%28with,modalfor,completionhandler%29.md)
  Presents a document-modal PDF panel.
### Constants
- [NSPDFPanel.Options](./nspdfpanel/options-swift.struct.md)
  Constants used to configure the contents of a PDF panel.
### Creating a PDF Panel
- [+ panel](./nspdfpanel/panel.md)
  Returns a new `NSPDFPanel` object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Print and PDF Panels
- [protocol NSPrintPanelAccessorizing](./nsprintpanelaccessorizing.md)
  A set of methods that a Print panel object can use to get information from a printing accessory controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspdfpanel)*