# textRange(for:enclosing:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns a text range that corresponds to selection granularity of the enclosing location.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func textRange(for selectionGranularity: NSTextSelection.Granularity, enclosing location: any NSTextLocation) -> NSTextRange?
```

#### Return Value

Returns the text range of the section, or `nil` when `documentRange.isEmpty` `true`.

## Parameters

- `selectionGranularity`: One of the possible   options.
- `location`: A location that encloses the text range of interest.

## See Also

- [func location(any NSTextLocation, offsetBy: Int) -> (any NSTextLocation)?](nstextselectiondatasource/location(_:offsetby:).md)
  Returns a new location using the location and offset you specify.
- [func lineFragmentRange(for: CGPoint, inContainerAt: any NSTextLocation) -> NSTextRange?](nstextselectiondatasource/linefragmentrange(for:incontainerat:).md)
  Returns the range of the line fragment that contains the point you specify.
- [func offset(from: any NSTextLocation, to: any NSTextLocation) -> Int](nstextselectiondatasource/offset(from:to:).md)
  Returns the offset between the two locations you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectiondatasource/textrange(for:enclosing:))*