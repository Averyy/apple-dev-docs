# textFinderCaseInsensitiveKey

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the search is case insensitive.

**Availability**:
- macOS 10.7+

## Declaration

```swift
static let textFinderCaseInsensitiveKey: NSPasteboard.PasteboardType.TextFinderOptionKey
```

#### Discussion

The value of this key must be an [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) object containing a Boolean value. The value [`true`](https://developer.apple.com/documentation/swift/true) indicates a case-insensitive search; [`false`](https://developer.apple.com/documentation/swift/false) indicates a case-sensitive search.

## See Also

- [static let textFinderMatchingTypeKey: NSPasteboard.PasteboardType.TextFinderOptionKey](nspasteboard/pasteboardtype/textfinderoptionkey/textfindermatchingtypekey.md)
  A number object containing the match type to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/pasteboardtype/textfinderoptionkey/textfindercaseinsensitivekey)*