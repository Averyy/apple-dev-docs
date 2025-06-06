# titleWidth(_:)

**Framework**: AppKit  
**Kind**: method

Returns the width of the title field constrained to the specified size.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func titleWidth(_ size: NSSize) -> CGFloat
```

#### Return Value

The width of the title field, measured in points in the user coordinate space.

#### Discussion

If you set the width using [`titleWidth`](nsformcell/titlewidth.md), this method returns the value you set; otherwise, the Application Kit calculates the width, constraining the field size to the specified value.

## Parameters

- `size`: The maximum size of the field when calculated by the Application Kit.

## See Also

- [var titleWidth: CGFloat](nsformcell/titlewidth.md)
  The width of the title field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsformcell/titlewidth(_:))*