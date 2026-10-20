# isEnabled(forSegment:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the specified segment is enabled.

**Availability**:
- macOS

## Declaration

```swift
func isEnabled(forSegment segment: Int) -> Bool
```

```objc
- (BOOL) isEnabledForSegment:(NSInteger) segment;
```

#### Return Value

[`true`](../../Swift/true.md) if the segment is enabled; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `segment`: The index of the segment whose enabled state you want to get. This method raises an exception ([`rangeException`](../../Foundation/nsexceptionname/rangeexception.md)) if the index is out of bounds.

## See Also

### Enabling and disabling segments
- [func setEnabled(Bool, forSegment: Int)](./setenabled%28_,forsegment%29.md)
  Sets the enabled state of the specified segment


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/isenabled(forsegment:))*