# label(forSegment:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the label of the specified segment.

**Availability**:
- macOS

## Declaration

```swift
func label(forSegment segment: Int) -> String?
```

```objc
- (NSString *) labelForSegment:(NSInteger) segment;
```

## Return Value

The label of the segment. The returned string contains the entire text of the label, even if that text is normally truncated during drawing.

## Parameters

- `segment`: The index of the segment whose label you want to get. This method raises an exception ([`rangeException`](../../Foundation/nsexceptionname/rangeexception.md)) if the index is out of bounds.

## See Also

### Configuring the segment text
- [func setLabel(String, forSegment: Int)](./setlabel%28_,forsegment%29.md)
  Sets the label for the specified segment.
- [func setAlignment(NSTextAlignment, forSegment: Int)](./setalignment%28_,forsegment%29.md)
- [func alignment(forSegment: Int) -> NSTextAlignment](./alignment%28forsegment%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/label(forsegment:))*