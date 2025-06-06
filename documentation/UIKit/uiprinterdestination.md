# UIPrinterDestination

**Framework**: UIKit  
**Kind**: class

A description of a single printer.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIPrinterDestination
```

#### Overview

You can use `UIPrinterDestination` to describe a printer so that it populates in a [`UIPrinterPickerController`](uiprinterpickercontroller.md) when the printer’s capabilities match the print-job attributes. `UIPrinterDestination` requires a URL to locate the printer. You can include an optional display name that populates in the user interface and a TXT record to detail the printer’s additional features.

## Topics

### Creating a printer destination
- [init(url: URL)](uiprinterdestination/init(url:).md)
  Creates a printer destination with the specified address.
### Describing the printer
- [var displayName: String?](uiprinterdestination/displayname.md)
  A human-readable string that displays the name of a printer.
- [var txtRecord: Data?](uiprinterdestination/txtrecord.md)
  A DNS TXT record to identify the printer.
- [var url: URL](uiprinterdestination/url.md)
  The address of the printer.

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
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIPrintServiceExtension](uiprintserviceextension.md)
  An extension that locates and sets up a printer without a configuration profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinterdestination)*