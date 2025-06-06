# location(_:offsetBy:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns a new location using the location and offset you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func location(_ location: any NSTextLocation, offsetBy offset: Int) -> (any NSTextLocation)?
```

#### Return Value

A new `NSTextLocation, or nil` when the inputs don’t produce any legal location, such as when the input is an out of bounds index.

#### Discussion

The offset value can be positive or negative indicating the logical direction.

## Parameters

- `location`: The starting location in the selection.
- `offset`: An offset that describes the extent of the new location.

## See Also

- [func lineFragmentRange(for: CGPoint, inContainerAt: any NSTextLocation) -> NSTextRange?](nstextselectiondatasource/linefragmentrange(for:incontainerat:).md)
  Returns the range of the line fragment that contains the point you specify.
- [func offset(from: any NSTextLocation, to: any NSTextLocation) -> Int](nstextselectiondatasource/offset(from:to:).md)
  Returns the offset between the two locations you specify.
- [func textRange(for: NSTextSelection.Granularity, enclosing: any NSTextLocation) -> NSTextRange?](nstextselectiondatasource/textrange(for:enclosing:).md)
  Returns a text range that corresponds to selection granularity of the enclosing location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectiondatasource/location(_:offsetby:))*