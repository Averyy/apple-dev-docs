# adjustedRange(from:forEditingTextSelection:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the text range, if any, in the backing store that required manual adjustment after editing.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func adjustedRange(from textRange: NSTextRange, forEditingTextSelection: Bool) -> NSTextRange?
```

```objc
- (NSTextRange *) adjustedRangeFromRange:(NSTextRange *) textRange forEditingTextSelection:(BOOL) forEditingTextSelection;
```

## Return Value

The  adjusted `TextRange` for the editing session, or `nil` of no adjustment was necessary

## Discussion

When `textRange` is intersecting or following the current edited range, the method returns an adjusted range for the modification in the editing session.

## Parameters

- `textRange`: The text range.
- `forEditingTextSelection`: A Boolean value that indicates if `textRange` is for the text selection associated with the edit session.

## See Also

### Finding ranges, locations, and offsets
- [func location(any NSTextLocation, offsetBy: Int) -> (any NSTextLocation)?](./location%28_,offsetby%29.md)
  Returns a new text location object based on an existing location and offset you provide.
- [func offset(from: any NSTextLocation, to: any NSTextLocation) -> Int](./offset%28from,to%29.md)
  Returns the number of characters between the specified locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextcontentstorage/adjustedrange(from:foreditingtextselection:))*