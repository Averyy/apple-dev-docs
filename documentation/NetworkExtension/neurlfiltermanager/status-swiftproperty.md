# status

**Framework**: Network Extension  
**Kind**: property

The current status of the URL filter.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
var status: NEURLFilterManager.Status { get async }
```

## See Also

- [func handleStatusChange() -> any AsyncSequence<NEURLFilterManager.Status, Never>](neurlfiltermanager/handlestatuschange.md)
  Sets up an observer for the status notification and models it as an asynchronous sequence.
- [NEURLFilterManager.Status](neurlfiltermanager/status-swift.enum.md)
  An enumeration of URL filter status codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/status-swift.property)*