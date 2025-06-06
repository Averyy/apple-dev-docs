# UIPrintServiceExtension

**Framework**: UIKit  
**Kind**: class

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

#### Overview

Support cloud printing by creating an extension instead of requiring users to install a managed configuration profile to set up an AirPrint printer. Create an extension by subclassing `UIPrintServiceExtension`. By creating your own extension, you can expose a cloud printer destination to a [`UIPrinterPickerController`](uiprinterpickercontroller.md). The extension matches printer destinations that fulfill the specified print-job attributes.

Create an instance of `UIPrinterDestination` to describe a printer to the system. The extension can then search for the printer, or set of printers, using [`printerDestinations(for:)`](uiprintserviceextension/printerdestinations(for:).md). This method matches the requirements of a [`UIPrintInfo`](uiprintinfo.md) object and returns an array of [`UIPrinterDestination`](uiprinterdestination.md).

## Topics

### Locating a printer
- [func printerDestinations(for: UIPrintInfo) -> [UIPrinterDestination]](uiprintserviceextension/printerdestinations(for:).md)
  Searches for a printer destination that matches the print-job attributes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [App extensions](app-extensions.md)
  Extend your app’s basic functionality to other parts of the system.
- [class UIPrinterDestination](uiprinterdestination.md)
  A description of a single printer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintserviceextension)*