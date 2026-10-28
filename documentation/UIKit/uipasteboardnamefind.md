# UIPasteboardNameFind

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

A name that identifies the Find pasteboard.

**Availability**:
- iOS 3.0+ - Deprecated in 10.0
- iPadOS 3.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: The Find pasteboard is no longer available.

## Declaration

```swift
let UIPasteboardNameFind: String
```

```c
extern NSString * const UIPasteboardNameFind;
```

## Discussion

The Find pasteboard is unavailable starting in iOS 10.

The name identifying the Find pasteboard, which, prior to iOS 10, was used in search operations. In such operations, the most recent search string in the search bar was put in the Find pasteboard.

## See Also

### Constants
- [static let general: UIPasteboard.Name](./uipasteboard/name-swift.struct/general.md)
  The name identifying the general pasteboard, which you use for general copy-cut-paste operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboardnamefind)*