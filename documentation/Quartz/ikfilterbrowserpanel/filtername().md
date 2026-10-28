# filterName()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the name of the  filter that is currently selected in the filter browser.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func filterName() -> String!
```

```objc
- (NSString *) filterName;
```

## Return Value

The name of the currently selected filter.

## Discussion

Use this method in response to the notifications [`IKFilterBrowserFilterSelectedNotification`](../ikfilterbrowserfilterselectednotification.md) or [`IKFilterBrowserFilterDoubleClickNotification`](../ikfilterbrowserfilterdoubleclicknotification.md), or after the user makes a choice in a dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikfilterbrowserpanel/filtername())*