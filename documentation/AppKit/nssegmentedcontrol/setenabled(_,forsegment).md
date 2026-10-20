# setEnabled(_:forSegment:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the enabled state of the specified segment

**Availability**:
- macOS

## Declaration

```swift
func setEnabled(_ enabled: Bool, forSegment segment: Int)
```

```objc
- (void) setEnabled:(BOOL) enabled forSegment:(NSInteger) segment;
```

## Parameters

- `enabled`: [`true`](../../Swift/true.md) to enable the segment; otherwise, [`false`](../../Swift/false.md) to disable it.
- `segment`: The index of the segment you want to enable or disable. This method raises an exception ([`rangeException`](../../Foundation/nsexceptionname/rangeexception.md)) if the index is out of bounds.

## See Also

### Enabling and disabling segments
- [func isEnabled(forSegment: Int) -> Bool](./isenabled%28forsegment%29.md)
  Returns a Boolean value indicating whether the specified segment is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/setenabled(_:forsegment:))*