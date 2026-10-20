# UIPrinterDestination

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UIPrinterDestination : NSObject
```

#### Overview

You can use `UIPrinterDestination` to describe a printer so that it populates in a [`UIPrinterPickerController`](./uiprinterpickercontroller.md) when the printer’s capabilities match the print-job attributes. `UIPrinterDestination` requires a URL to locate the printer. You can include an optional display name that populates in the user interface and a TXT record to detail the printer’s additional features.

## Topics

### Creating a printer destination
- [init(url: URL)](./uiprinterdestination/init%28url%29-7ck5j.md)
  Creates a printer destination with the specified address.
### Describing the printer
- [var displayName: String?](./uiprinterdestination/displayname.md)
  A human-readable string that displays the name of a printer.
- [var txtRecord: Data?](./uiprinterdestination/txtrecord.md)
  A DNS TXT record to identify the printer.
- [var url: URL](./uiprinterdestination/url.md)
  The address of the printer.
### Initializers
- [init(URL: URL)](./uiprinterdestination/init%28url%29-c1e8.md)
- [init?(coder: NSCoder)](./uiprinterdestination/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Printer service discovery
- [class UIPrintServiceExtension](./uiprintserviceextension.md)
  An extension that locates and sets up a printer without a configuration profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinterdestination)*