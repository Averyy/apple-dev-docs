# setLabel(_:forSegment:)

**Framework**: AppKit  
**Kind**: method

Sets the label for the specified segment.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setLabel(_ label: String, forSegment segment: Int)
```

## Parameters

- `label`: The label you want to display in the segment. If the width of the string is greater than the width of the segment, the string’s text is truncated during drawing.
- `segment`: The index of the segment whose label you want to set. This method raises an exception ( ) if the index is out of bounds.

## See Also

- [func label(forSegment: Int) -> String?](nssegmentedcontrol/label(forsegment:).md)
  Returns the label of the specified segment.
- [func setAlignment(NSTextAlignment, forSegment: Int)](nssegmentedcontrol/setalignment(_:forsegment:).md)
- [func alignment(forSegment: Int) -> NSTextAlignment](nssegmentedcontrol/alignment(forsegment:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/setlabel(_:forsegment:))*