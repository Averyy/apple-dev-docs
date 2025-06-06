# displayName

**Framework**: UIKit  
**Kind**: property

A human-readable string that displays the name of a printer.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var displayName: String? { get set }
```

#### Discussion

This property contains a name that describes the printer’s manufacturer and model number to display in the app’s user interface. If `nil`, the [`txtRecord`](uiprinterdestination/txtrecord.md) property can produce the display name.

## See Also

- [var txtRecord: Data?](uiprinterdestination/txtrecord.md)
  A DNS TXT record to identify the printer.
- [var url: URL](uiprinterdestination/url.md)
  The address of the printer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinterdestination/displayname)*