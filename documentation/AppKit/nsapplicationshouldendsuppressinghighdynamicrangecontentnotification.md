# NSApplicationShouldEndSuppressingHighDynamicRangeContentNotification

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- macOS 26.0+

## Declaration

```c
extern NSNotificationName NSApplicationShouldEndSuppressingHighDynamicRangeContentNotification;
```

## See Also

### Displaying high dynamic resolution (HDR) content
- [var applicationShouldSuppressHighDynamicRangeContent: Bool](./nsapplication/applicationshouldsuppresshighdynamicrangecontent.md)
  A boolean value indicating whether your application should suppress HDR content based on established policy. Built-in AppKit components such as NSImageView will automatically behave correctly with HDR content. You should use this value in conjunction with notifications (`NSApplicationShouldBeginSuppressingHighDynamicRangeContentNotification` and `NSApplicationShouldEndSuppressingHighDynamicRangeContentNotification`) to suppress HDR content in your application when signaled to do so.
- [NSApplicationShouldBeginSuppressingHighDynamicRangeContentNotification](./nsapplicationshouldbeginsuppressinghighdynamicrangecontentnotification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationshouldendsuppressinghighdynamicrangecontentnotification)*