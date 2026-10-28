# sizeOfLabel(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Calculates the size of the receiver’s label.

**Availability**:
- macOS

## Declaration

```swift
func sizeOfLabel(_ computeMin: Bool) -> NSSize
```

```objc
- (NSSize) sizeOfLabel:(BOOL) computeMin;
```

## Discussion

If `shouldTruncateLabel` is [`false`](../../Swift/false.md), returns the size of the receiver’s full label. If `shouldTruncateLabel` is [`true`](../../Swift/true.md), returns the truncated size. If your application does anything to change the size of tab labels, such as overriding the [`drawLabel(_:in:)`](./drawlabel%28_,in%29.md) method to add an icon to each tab, you should override [`sizeOfLabel(_:)`](./sizeoflabel%28_%29.md) too so the NSTabView knows the correct size for the tab label.

## See Also

### Related Documentation
- [var font: NSFont](../nstabview/font.md)
  The font used for the tab view’s label text.
### Working with Labels
- [func drawLabel(Bool, in: NSRect)](./drawlabel%28_,in%29.md)
  Draws the receiver’s label in `tabRect`, which is the area between the curved end caps.
- [var label: String](./label.md)
  Sets the label text for the receiver to `label`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewitem/sizeoflabel(_:))*