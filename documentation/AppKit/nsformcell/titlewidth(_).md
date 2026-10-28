# titleWidth(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the width of the title field constrained to the specified size.

**Availability**:
- macOS

## Declaration

```swift
func titleWidth(_ size: NSSize) -> CGFloat
```

```objc
- (CGFloat) titleWidth:(NSSize) size;
```

## Return Value

The width of the title field, measured in points in the user coordinate space.

## Discussion

If you set the width using [`titleWidth`](./titlewidth.md), this method returns the value you set; otherwise, the Application Kit calculates the width, constraining the field size to the specified value.

## Parameters

- `size`: The maximum size of the field when calculated by the Application Kit.

## See Also

### Related Documentation
- [var titleWidth: CGFloat](./titlewidth.md)
  The width of the title field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsformcell/titlewidth(_:))*