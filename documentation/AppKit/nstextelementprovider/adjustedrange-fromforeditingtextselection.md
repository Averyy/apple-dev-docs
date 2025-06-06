# adjustedRange(from:forEditingTextSelection:)

**Framework**: AppKit  
**Kind**: method

A method you implement if the location backing store requires manual adjustment after editing.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func adjustedRange(from textRange: NSTextRange, forEditingTextSelection: Bool) -> NSTextRange?
```

#### Return Value

When `textRange` is intersecting or following the current edited range, the method returns the range adjusted for the modification in the editing session. Returns `nil`, when no adjustment necessary.

## Parameters

- `textRange`: An   that the method adjusts.
- `forEditingTextSelection`: A Boolean value that indicates if   is for the text selection associated with the edit session.

## See Also

- [func offset(from: any NSTextLocation, to: any NSTextLocation) -> Int](nstextelementprovider/offset(from:to:).md)
  Returns the offset between the two specified locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextelementprovider/adjustedrange(from:foreditingtextselection:))*