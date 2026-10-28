# enumerateCaretOffsetsInLineFragment(at:using:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Enumerates all the insertion point caret offsets from left to right in visual order.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func enumerateCaretOffsetsInLineFragment(at location: any NSTextLocation, using block: (CGFloat, any NSTextLocation, Bool, UnsafeMutablePointer<ObjCBool>) -> Void)
```

```objc
- (void) enumerateCaretOffsetsInLineFragmentAtLocation:(id<NSTextLocation>) location usingBlock:(void (^)(CGFloat caretOffset, id<NSTextLocation>location, BOOL leadingEdge, BOOL *stop)) block;
```

## Discussion

The `caretOffset` is in the coordinate system for the text container. When `leadingEdge` is `true`, it indicates that `caretOffset` is at the logical edge preceding the character. For left-to-right characters, the caret is on the left, and on the right for right-to-left characters.

## Parameters

- `location`: The `NSTextLocation` to start from.
- `block`: The closure to invoke once for each logical caret edge in the line fragment, in left-to-right visual order. End the enumeration early by returning `false`.

## See Also

### Enumerating components of the selection
- [func enumerateContainerBoundaries(from: any NSTextLocation, reverse: Bool, using: (any NSTextLocation, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratecontainerboundaries%28from,reverse,using%29.md)
  Enumerates all the container boundaries starting from the location you specify.
- [func enumerateSubstrings(from: any NSTextLocation, options: NSString.EnumerationOptions, using: (String?, NSTextRange, NSTextRange?, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratesubstrings%28from,options,using%29.md)
  Enumerates the textual segment boundaries starting at the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectiondatasource/enumeratecaretoffsetsinlinefragment(at:using:))*