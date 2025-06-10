# NSApplication.ShouldEndSuppressingHighDynamicRangeContent

**Framework**: AppKit  
**Kind**: struct

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
struct ShouldEndSuppressingHighDynamicRangeContent
```

## Topics

### Creating a notification
- [static func makeNotification(NSApplication.ShouldEndSuppressingHighDynamicRangeContent) -> Notification](nsapplication/shouldendsuppressinghighdynamicrangecontent/makenotification(_:).md)

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../Foundation/NotificationCenter/MainActorMessage.md)
- [NotificationCenter.Message](../Foundation/NotificationCenter/Message.md)

## See Also

- [var applicationShouldSuppressHighDynamicRangeContent: Bool](nsapplication/applicationshouldsuppresshighdynamicrangecontent.md)
  A boolean value indicating whether your application should suppress HDR content based on established policy. Built-in AppKit components such as NSImageView will automatically behave correctly with HDR content. You should use this value in conjunction with notifications (`NSApplicationShouldBeginSuppressingHighDynamicRangeContentNotification` and `NSApplicationShouldEndSuppressingHighDynamicRangeContentNotification`) to suppress HDR content in your application when signaled to do so.
- [NSApplication.ShouldBeginSuppressingHighDynamicRangeContent](nsapplication/shouldbeginsuppressinghighdynamicrangecontent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/shouldendsuppressinghighdynamicrangecontent)*