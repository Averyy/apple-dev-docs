# expirationDate

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The time and date that you want the system to remove the pasteboard items from the pasteboard.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
static let expirationDate: UIPasteboard.OptionsKey
```

```c
extern UIPasteboardOption const UIPasteboardOptionExpirationDate;
```

#### Discussion

Specify the date and time as an [`NSDate`](../../../Foundation/nsdate.md) value.

## See Also

### Constants
- [static let localOnly: UIPasteboard.OptionsKey](./localonly.md)
  A Boolean value that specifies that the pasteboard items should not be available to other devices through the Handoff feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/optionskey/expirationdate)*