# IKFilterBrowserWillPreviewFilterNotification

**Framework**: Quartz  
**Kind**: var  
**Role**: Global Variable

Posted before showing a filter preview, allowing an application to set the parameters of a filter.

**Availability**:
- macOS 10.4+

## Declaration

```c
extern NSString * const IKFilterBrowserWillPreviewFilterNotification;
```

#### Discussion

The selected filter is sent as the object in the notification.

## See Also

### Notifications
- [IKFilterBrowserFilterSelectedNotification](./ikfilterbrowserfilterselectednotification.md)
  Posted when the user clicks a filter name in the filter browser.
- [IKFilterBrowserFilterDoubleClickNotification](./ikfilterbrowserfilterdoubleclicknotification.md)
  Posted when the user double-clicks a filter in the filter browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikfilterbrowserwillpreviewfilternotification)*