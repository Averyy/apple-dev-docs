# offset(from:to:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns the offset between the two locations you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func offset(from: any NSTextLocation, to: any NSTextLocation) -> Int
```

## Parameters

- `from`: The starting location.
- `to`: The ending location.

## See Also

- [func location(any NSTextLocation, offsetBy: Int) -> (any NSTextLocation)?](nstextselectiondatasource/location(_:offsetby:).md)
  Returns a new location using the location and offset you specify.
- [func lineFragmentRange(for: CGPoint, inContainerAt: any NSTextLocation) -> NSTextRange?](nstextselectiondatasource/linefragmentrange(for:incontainerat:).md)
  Returns the range of the line fragment that contains the point you specify.
- [func textRange(for: NSTextSelection.Granularity, enclosing: any NSTextLocation) -> NSTextRange?](nstextselectiondatasource/textrange(for:enclosing:).md)
  Returns a text range that corresponds to selection granularity of the enclosing location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectiondatasource/offset(from:to:))*