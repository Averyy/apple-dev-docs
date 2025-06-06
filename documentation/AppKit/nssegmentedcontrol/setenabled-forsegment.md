# setEnabled(_:forSegment:)

**Framework**: AppKit  
**Kind**: method

Sets the enabled state of the specified segment

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setEnabled(_ enabled: Bool, forSegment segment: Int)
```

## Parameters

- `enabled`:   to enable the segment; otherwise,   to disable it.
- `segment`: The index of the segment you want to enable or disable. This method raises an exception ( ) if the index is out of bounds.

## See Also

- [func isEnabled(forSegment: Int) -> Bool](nssegmentedcontrol/isenabled(forsegment:).md)
  Returns a Boolean value indicating whether the specified segment is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/setenabled(_:forsegment:))*