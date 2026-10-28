# IKFilterBrowserFilterSelectedNotification

**Framework**: Quartz  
**Kind**: var  
**Role**: Global Variable

Posted when the user clicks a filter name in the filter browser.

**Availability**:
- macOS 10.4+

## Declaration

```c
extern NSString * const IKFilterBrowserFilterSelectedNotification;
```

## Discussion

The name of the selected filter is sent as the object in the notification.

## See Also

### Notifications
- [IKFilterBrowserWillPreviewFilterNotification](./ikfilterbrowserwillpreviewfilternotification.md)
  Posted before showing a filter preview, allowing an application to set the parameters of a filter.
- [IKFilterBrowserFilterDoubleClickNotification](./ikfilterbrowserfilterdoubleclicknotification.md)
  Posted when the user double-clicks a filter in the filter browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikfilterbrowserfilterselectednotification)*