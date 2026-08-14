# menuChangedMessagesEnabled

**Framework**: AppKit  
**Kind**: property

Indicates whether messages are sent to the application’s windows each time the menu changes.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var menuChangedMessagesEnabled: Bool { get set }
```

#### Discussion

This property indicates whether messages are sent to the application’s windows each time the menu changes.

To avoid the “flickering” effect of many successive menu changes, set the value of this property to [`false`](https://developer.apple.com/documentation/swift/false), make changes to the menu, and then set the value of this property to [`true`](https://developer.apple.com/documentation/swift/true). This approach has the effect of batching changes and applying them all at once.

##### Special Considerations

In macOS 10.6 and later this property has no effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/menuchangedmessagesenabled)*