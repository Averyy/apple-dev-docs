# lastDisconnectError

**Framework**: Network Extension  
**Kind**: property

The most recent error that caused the URL Filter to stop.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
var lastDisconnectError: NEURLFilterManager.Error? { get async }
```

#### Discussion

You can check this property after an unexpected status change to determine what caused the filter to stop.

> 💡 **Tip**: This value may be a remnant of a previously-encountered issue, if nothing has caused a more recent error to overwrite it.

## See Also

- [NEURLFilterManager.Error](neurlfiltermanager/error.md)
  An enumeration of URL filter error codes


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/lastdisconnecterror)*