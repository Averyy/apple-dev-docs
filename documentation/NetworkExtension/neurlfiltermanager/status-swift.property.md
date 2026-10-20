# status

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The current status of the URL filter.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var status: NEURLFilterManager.Status { get async }
```

## See Also

### Working with filter statuses
- [func handleStatusChange() -> any AsyncSequence<NEURLFilterManager.Status, Never>](./handlestatuschange%28%29.md)
  Sets up an observer for the status notification and models it as an asynchronous sequence.
- [NEURLFilterManager.Status](./status-swift.enum.md)
  An enumeration of URL filter status codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/status-swift.property)*