# enumerateCaretOffsetsInLineFragment(at:using:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Enumerates all the insertion point caret offsets from left to right in visual order.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func enumerateCaretOffsetsInLineFragment(at location: any NSTextLocation, using block: (CGFloat, any NSTextLocation, Bool, UnsafeMutablePointer<ObjCBool>) -> Void)
```

#### Discussion

The `caretOffset` is in the coordinate system for the text container. When `leadingEdge` is `true`, it indicates that `caretOffset` is at the logical edge preceding the character. For left-to-right characters, the caret is on the left, and on the right for right-to-left characters.

## Parameters

- `location`: The   to start from.
- `block`: The closure to invoke once for each logical caret edge in the line fragment, in left-to-right visual order. End the enumeration early by returning  .

## See Also

- [func enumerateContainerBoundaries(from: any NSTextLocation, reverse: Bool, using: (any NSTextLocation, UnsafeMutablePointer<ObjCBool>) -> Void)](nstextselectiondatasource/enumeratecontainerboundaries(from:reverse:using:).md)
  Enumerates all the container boundaries starting from the location you specify.
- [func enumerateSubstrings(from: any NSTextLocation, options: NSString.EnumerationOptions, using: (String?, NSTextRange, NSTextRange?, UnsafeMutablePointer<ObjCBool>) -> Void)](nstextselectiondatasource/enumeratesubstrings(from:options:using:).md)
  Enumerates the textual segment boundaries starting at the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectiondatasource/enumeratecaretoffsetsinlinefragment(at:using:))*