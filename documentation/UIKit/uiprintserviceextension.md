# UIPrintServiceExtension

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An extension that locates and sets up a printer without a configuration profile.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIPrintServiceExtension
```

```objc
@interface UIPrintServiceExtension : NSObject
```

## Overview

Support cloud printing by creating an extension instead of requiring users to install a managed configuration profile to set up an AirPrint printer. Create an extension by subclassing `UIPrintServiceExtension`. By creating your own extension, you can expose a cloud printer destination to a [`UIPrinterPickerController`](./uiprinterpickercontroller.md). The extension matches printer destinations that fulfill the specified print-job attributes.

Create an instance of `UIPrinterDestination` to describe a printer to the system. The extension can then search for the printer, or set of printers, using [`printerDestinations(for:)`](./uiprintserviceextension/printerdestinations%28for%29.md). This method matches the requirements of a [`UIPrintInfo`](./uiprintinfo.md) object and returns an array of [`UIPrinterDestination`](./uiprinterdestination.md).

## Topics

### Locating a printer
- [func printerDestinations(for: UIPrintInfo) -> [UIPrinterDestination]](./uiprintserviceextension/printerdestinations%28for%29.md)
  Searches for a printer destination that matches the print-job attributes.

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

### Related Documentation
- [App extensions](./app-extensions.md)
  Extend your app’s basic functionality to other parts of the system.
### Printer service discovery
- [class UIPrinterDestination](./uiprinterdestination.md)
  A description of a single printer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintserviceextension)*