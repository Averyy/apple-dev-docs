# enumerateContainerBoundaries(from:reverse:using:)

**Framework**: UIKit  
**Kind**: method

Enumerates all the container boundaries starting from the location you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
optional func enumerateContainerBoundaries(from location: any NSTextLocation, reverse: Bool, using block: (any NSTextLocation, UnsafeMutablePointer<ObjCBool>) -> Void)
```

#### Discussion

This is an optional method you implement to enumerate the text up to the container or page boundary when the text selection data provider supports this layout functionality.

## Parameters

- `location`: The location where the enumeration starts.
- `reverse`: A Boolean value that indicates the enumeration starts at the end of the container.
- `block`: AA closure to invoke to evaluate the container boundaries; end the enumeration early by returning  .

## See Also

- [func enumerateCaretOffsetsInLineFragment(at: any NSTextLocation, using: (CGFloat, any NSTextLocation, Bool, UnsafeMutablePointer<ObjCBool>) -> Void)](nstextselectiondatasource/enumeratecaretoffsetsinlinefragment(at:using:).md)
  Enumerates all the insertion point caret offsets from left to right in visual order.
- [func enumerateSubstrings(from: any NSTextLocation, options: NSString.EnumerationOptions, using: (String?, NSTextRange, NSTextRange?, UnsafeMutablePointer<ObjCBool>) -> Void)](nstextselectiondatasource/enumeratesubstrings(from:options:using:).md)
  Enumerates the textual segment boundaries starting at the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectiondatasource/enumeratecontainerboundaries(from:reverse:using:))*