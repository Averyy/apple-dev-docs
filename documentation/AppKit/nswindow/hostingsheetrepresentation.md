# NSWindow.HostingSheetRepresentation

**Framework**: AppKit  
**Kind**: class

A class representing a SwiftUI view hosted in an AppKit sheet.

**Availability**:
- macOS 26.0+

## Declaration

```swift
class HostingSheetRepresentation<Content> where Content : View
```

#### Overview

This is created and returned by [`beginSheet(content:completionHandler:)`](nswindow/beginsheet(content:completionhandler:).md) as a representation of the presented sheet. It can be used to change the root view of the sheet while presented or be used to programamtically dismiss the sheet from an AppKit context using [`endSheet(_:)`](nswindow/endsheet(_:)-6af2u.md).

## Topics

### Instance Properties
- [var rootView: Content](nswindow/hostingsheetrepresentation/rootview.md)
  The root view of the sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/hostingsheetrepresentation)*