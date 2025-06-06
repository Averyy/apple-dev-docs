# adjustedRange(from:forEditingTextSelection:)

**Framework**: AppKit  
**Kind**: method

Returns the text range, if any, in the backing store that required manual adjustment after editing.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func adjustedRange(from textRange: NSTextRange, forEditingTextSelection: Bool) -> NSTextRange?
```

#### Return Value

The  adjusted `TextRange` for the editing session, or `nil` of no adjustment was necessary

#### Discussion

When `textRange` is intersecting or following the current edited range, the method returns an adjusted range for the modification in the editing session.

## Parameters

- `textRange`: The text range.
- `forEditingTextSelection`: A Boolean value that indicates if   is for the text selection associated with the edit session.

## See Also

- [func location(any NSTextLocation, offsetBy: Int) -> (any NSTextLocation)?](nstextcontentstorage/location(_:offsetby:).md)
  Returns a new text location object based on an existing location and offset you provide.
- [func offset(from: any NSTextLocation, to: any NSTextLocation) -> Int](nstextcontentstorage/offset(from:to:).md)
  Returns the number of characters between the specified locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontentstorage/adjustedrange(from:foreditingtextselection:))*