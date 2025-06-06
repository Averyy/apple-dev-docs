# filterName()

**Framework**: Quartz  
**Kind**: method

Returns the name of the  filter that is currently selected in the filter browser.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func filterName() -> String!
```

#### Return Value

The name of the currently selected filter.

#### Discussion

Use this method in response to the notifications [`IKFilterBrowserFilterSelectedNotification`](ikfilterbrowserfilterselectednotification.md) or [`IKFilterBrowserFilterDoubleClickNotification`](ikfilterbrowserfilterdoubleclicknotification.md), or after the user makes a choice in a dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikfilterbrowserview/filtername())*