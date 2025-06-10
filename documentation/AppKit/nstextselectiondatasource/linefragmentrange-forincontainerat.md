# lineFragmentRange(for:inContainerAt:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the range of the line fragment that contains the point you specify.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func lineFragmentRange(for point: CGPoint, inContainerAt location: any NSTextLocation) -> NSTextRange?
```

#### Return Value

An `NSTextRange` that describes the location of the line fragment, or nil if the range isn’t found.

## Parameters

- `point`: The starting point that contains the line fragment, in the coordinate system of  .
- `location`: The location of the line fragment.

## See Also

- [func location(any NSTextLocation, offsetBy: Int) -> (any NSTextLocation)?](nstextselectiondatasource/location(_:offsetby:).md)
  Returns a new location using the location and offset you specify.
- [func offset(from: any NSTextLocation, to: any NSTextLocation) -> Int](nstextselectiondatasource/offset(from:to:).md)
  Returns the offset between the two locations you specify.
- [func textRange(for: NSTextSelection.Granularity, enclosing: any NSTextLocation) -> NSTextRange?](nstextselectiondatasource/textrange(for:enclosing:).md)
  Returns a text range that corresponds to selection granularity of the enclosing location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectiondatasource/linefragmentrange(for:incontainerat:))*