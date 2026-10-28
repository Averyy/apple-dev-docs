# localOnly

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A Boolean value that specifies that the pasteboard items should not be available to other devices through the Handoff feature.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
static let localOnly: UIPasteboard.OptionsKey
```

```c
extern UIPasteboardOption const UIPasteboardOptionLocalOnly;
```

## Description

The value is expressed as an [`NSNumber`](../../../Foundation/nsnumber.md) type.

## See Also

### Constants
- [static let expirationDate: UIPasteboard.OptionsKey](./expirationdate.md)
  The time and date that you want the system to remove the pasteboard items from the pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/optionskey/localonly)*