# enumerateSubstrings(from:options:using:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Enumerates the textual segment boundaries starting at the location you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func enumerateSubstrings(from location: any NSTextLocation, options: NSString.EnumerationOptions = [], using block: (String?, NSTextRange, NSTextRange?, UnsafeMutablePointer<ObjCBool>) -> Void)
```

#### Discussion

## Parameters

- `location`: The location where the enumeration starts.
- `options`: One or more of the available  .
- `block`: A closure to invoke to evaluate the substrings; end the enumeration early by returning  .

## See Also

- [func enumerateCaretOffsetsInLineFragment(at: any NSTextLocation, using: (CGFloat, any NSTextLocation, Bool, UnsafeMutablePointer<ObjCBool>) -> Void)](nstextselectiondatasource/enumeratecaretoffsetsinlinefragment(at:using:).md)
  Enumerates all the insertion point caret offsets from left to right in visual order.
- [func enumerateContainerBoundaries(from: any NSTextLocation, reverse: Bool, using: (any NSTextLocation, UnsafeMutablePointer<ObjCBool>) -> Void)](nstextselectiondatasource/enumeratecontainerboundaries(from:reverse:using:).md)
  Enumerates all the container boundaries starting from the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectiondatasource/enumeratesubstrings(from:options:using:))*