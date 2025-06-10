# handleStatusChange()

**Framework**: Network Extension  
**Kind**: method

Sets up an observer for the status notification and models it as an asynchronous sequence.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
func handleStatusChange() -> any AsyncSequence<NEURLFilterManager.Status, Never>
```

#### Discussion

The [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence) created by this method produces a new status every time the filter posts the [`NEURLFilterStatusDidChange`](https://developer.apple.com/documentation/Foundation/NSNotification/Name-swift.struct/NEURLFilterStatusDidChange) notification.

Use this method to watch for the status change notification and react to it.

## See Also

- [var status: NEURLFilterManager.Status](neurlfiltermanager/status-swift.property.md)
  The current status of the URL filter.
- [NEURLFilterManager.Status](neurlfiltermanager/status-swift.enum.md)
  An enumeration of URL filter status codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/handlestatuschange())*