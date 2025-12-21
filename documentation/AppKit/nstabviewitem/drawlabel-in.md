# drawLabel(_:in:)

**Framework**: AppKit  
**Kind**: method

Draws the receiver’s label in `tabRect`, which is the area between the curved end caps.

**Availability**:
- macOS ?+

## Declaration

```swift
func drawLabel(_ shouldTruncateLabel: Bool, in labelRect: NSRect)
```

#### Discussion

If `shouldTruncateLabel` is [`false`](https://developer.apple.com/documentation/Swift/false), draws the full label in the rectangle specified by `tabRect`. If `shouldTruncateLabel` is [`true`](https://developer.apple.com/documentation/Swift/true), draws the truncated label. You can override this method to perform customized label drawing. For example, you might want to add an icon to each tab in the view.

## See Also

- [var label: String](nstabviewitem/label.md)
  Sets the label text for the receiver to `label`.
- [func sizeOfLabel(Bool) -> NSSize](nstabviewitem/sizeoflabel(_:).md)
  Calculates the size of the receiver’s label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewitem/drawlabel(_:in:))*