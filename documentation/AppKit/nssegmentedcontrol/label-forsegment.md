# label(forSegment:)

**Framework**: AppKit  
**Kind**: method

Returns the label of the specified segment.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func label(forSegment segment: Int) -> String?
```

#### Return Value

The label of the segment. The returned string contains the entire text of the label, even if that text is normally truncated during drawing.

## Parameters

- `segment`: The index of the segment whose label you want to get. This method raises an exception ( ) if the index is out of bounds.

## See Also

- [func setLabel(String, forSegment: Int)](nssegmentedcontrol/setlabel(_:forsegment:).md)
  Sets the label for the specified segment.
- [func setAlignment(NSTextAlignment, forSegment: Int)](nssegmentedcontrol/setalignment(_:forsegment:).md)
- [func alignment(forSegment: Int) -> NSTextAlignment](nssegmentedcontrol/alignment(forsegment:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/label(forsegment:))*