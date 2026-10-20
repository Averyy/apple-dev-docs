# setLabel(_:forSegment:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the label for the specified segment.

**Availability**:
- macOS

## Declaration

```swift
func setLabel(_ label: String, forSegment segment: Int)
```

```objc
- (void) setLabel:(NSString *) label forSegment:(NSInteger) segment;
```

## Parameters

- `label`: The label you want to display in the segment. If the width of the string is greater than the width of the segment, the string’s text is truncated during drawing.
- `segment`: The index of the segment whose label you want to set. This method raises an exception ([`rangeException`](../../Foundation/nsexceptionname/rangeexception.md)) if the index is out of bounds.

## See Also

### Configuring the segment text
- [func label(forSegment: Int) -> String?](./label%28forsegment%29.md)
  Returns the label of the specified segment.
- [func setAlignment(NSTextAlignment, forSegment: Int)](./setalignment%28_,forsegment%29.md)
- [func alignment(forSegment: Int) -> NSTextAlignment](./alignment%28forsegment%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/setlabel(_:forsegment:))*