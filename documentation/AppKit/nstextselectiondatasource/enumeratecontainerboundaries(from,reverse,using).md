# enumerateContainerBoundaries(from:reverse:using:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Enumerates all the container boundaries starting from the location you specify.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func enumerateContainerBoundaries(from location: any NSTextLocation, reverse: Bool, using block: (any NSTextLocation, UnsafeMutablePointer<ObjCBool>) -> Void)
```

```objc
- (void) enumerateContainerBoundariesFromLocation:(id<NSTextLocation>) location reverse:(BOOL) reverse usingBlock:(void (^)(id<NSTextLocation>boundaryLocation, BOOL *stop)) block;
```

#### Discussion

This is an optional method you implement to enumerate the text up to the container or page boundary when the text selection data provider supports this layout functionality.

## Parameters

- `location`: The location where the enumeration starts.
- `reverse`: A Boolean value that indicates the enumeration starts at the end of the container.
- `block`: A closure to invoke to evaluate the container boundaries; end the enumeration early by returning `false`.

## See Also

### Enumerating components of the selection
- [func enumerateCaretOffsetsInLineFragment(at: any NSTextLocation, using: (CGFloat, any NSTextLocation, Bool, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratecaretoffsetsinlinefragment%28at,using%29.md)
  Enumerates all the insertion point caret offsets from left to right in visual order.
- [func enumerateSubstrings(from: any NSTextLocation, options: NSString.EnumerationOptions, using: (String?, NSTextRange, NSTextRange?, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratesubstrings%28from,options,using%29.md)
  Enumerates the textual segment boundaries starting at the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectiondatasource/enumeratecontainerboundaries(from:reverse:using:))*