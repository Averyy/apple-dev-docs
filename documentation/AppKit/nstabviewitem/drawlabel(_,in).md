# drawLabel(_:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the receiver’s label in `tabRect`, which is the area between the curved end caps.

**Availability**:
- macOS

## Declaration

```swift
func drawLabel(_ shouldTruncateLabel: Bool, in labelRect: NSRect)
```

```objc
- (void) drawLabel:(BOOL) shouldTruncateLabel inRect:(NSRect) labelRect;
```

#### Discussion

If `shouldTruncateLabel` is [`false`](../../Swift/false.md), draws the full label in the rectangle specified by `tabRect`. If `shouldTruncateLabel` is [`true`](../../Swift/true.md), draws the truncated label. You can override this method to perform customized label drawing. For example, you might want to add an icon to each tab in the view.

## See Also

### Working with Labels
- [var label: String](./label.md)
  Sets the label text for the receiver to `label`.
- [func sizeOfLabel(Bool) -> NSSize](./sizeoflabel%28_%29.md)
  Calculates the size of the receiver’s label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewitem/drawlabel(_:in:))*