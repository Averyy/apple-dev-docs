# NSApplication.ShouldBeginSuppressingHighDynamicRangeContent

**Framework**: AppKit  
**Kind**: struct

**Availability**:
- macOS 26.0+

## Declaration

```swift
struct ShouldBeginSuppressingHighDynamicRangeContent
```

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../Foundation/NotificationCenter/MainActorMessage.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var applicationShouldSuppressHighDynamicRangeContent: Bool](nsapplication/applicationshouldsuppresshighdynamicrangecontent.md)
  A boolean value indicating whether your application should suppress HDR content based on established policy. Built-in AppKit components such as NSImageView will automatically behave correctly with HDR content. You should use this value in conjunction with notifications (`NSApplicationShouldBeginSuppressingHighDynamicRangeContentNotification` and `NSApplicationShouldEndSuppressingHighDynamicRangeContentNotification`) to suppress HDR content in your application when signaled to do so.
- [NSApplication.ShouldEndSuppressingHighDynamicRangeContent](nsapplication/shouldendsuppressinghighdynamicrangecontent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/shouldbeginsuppressinghighdynamicrangecontent)*