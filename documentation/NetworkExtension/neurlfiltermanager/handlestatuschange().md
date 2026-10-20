# handleStatusChange()

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Sets up an observer for the status notification and models it as an asynchronous sequence.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
func handleStatusChange() -> any AsyncSequence<NEURLFilterManager.Status, Never>
```

#### Discussion

The [`AsyncSequence`](../../Swift/asyncsequence.md) created by this method produces a new status every time the filter posts the [`NEURLFilterStatusDidChange`](../../Foundation/nsnotification/name-swift.struct/neurlfilterstatusdidchange.md) notification.

Use this method to watch for the status change notification and react to it.

## See Also

### Working with filter statuses
- [var status: NEURLFilterManager.Status](./status-swift.property.md)
  The current status of the URL filter.
- [NEURLFilterManager.Status](./status-swift.enum.md)
  An enumeration of URL filter status codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/handlestatuschange())*