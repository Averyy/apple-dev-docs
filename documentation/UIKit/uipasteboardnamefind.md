# UIPasteboardNameFind

**Framework**: UIKit  
**Kind**: var

A name that identifies the Find pasteboard.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
let UIPasteboardNameFind: String
```

#### Discussion

The Find pasteboard is unavailable starting in iOS 10.

The name identifying the Find pasteboard, which, prior to iOS 10, was used in search operations. In such operations, the most recent search string in the search bar was put in the Find pasteboard.

## See Also

- [static let general: UIPasteboard.Name](uipasteboard/name-swift.struct/general.md)
  The name identifying the general pasteboard, which you use for general copy-cut-paste operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboardnamefind)*