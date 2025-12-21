# sizeOfLabel(_:)

**Framework**: AppKit  
**Kind**: method

Calculates the size of the receiver’s label.

**Availability**:
- macOS ?+

## Declaration

```swift
func sizeOfLabel(_ computeMin: Bool) -> NSSize
```

#### Discussion

If `shouldTruncateLabel` is [`false`](https://developer.apple.com/documentation/Swift/false), returns the size of the receiver’s full label. If `shouldTruncateLabel` is [`true`](https://developer.apple.com/documentation/Swift/true), returns the truncated size. If your application does anything to change the size of tab labels, such as overriding the [`drawLabel(_:in:)`](nstabviewitem/drawlabel(_:in:).md) method to add an icon to each tab, you should override [`sizeOfLabel(_:)`](nstabviewitem/sizeoflabel(_:).md) too so the NSTabView knows the correct size for the tab label.

## See Also

- [var font: NSFont](nstabview/font.md)
  The font used for the tab view’s label text.
- [func drawLabel(Bool, in: NSRect)](nstabviewitem/drawlabel(_:in:).md)
  Draws the receiver’s label in `tabRect`, which is the area between the curved end caps.
- [var label: String](nstabviewitem/label.md)
  Sets the label text for the receiver to `label`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewitem/sizeoflabel(_:))*