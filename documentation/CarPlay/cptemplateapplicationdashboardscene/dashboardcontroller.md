# dashboardController

**Framework**: CarPlay  
**Kind**: property

The controller that manages the dashboard scene’s shortcut buttons.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
@MainActor
var dashboardController: CPDashboardController { get }
```

#### Discussion

Use this property to access the controller CarPlay creates when it connects your navigation app’s dashboard scene. You use this controller to manage the shortcut buttons CarPlay displays in the dashboard when there’s no active navigation session.

## See Also

- [class CPDashboardController](cpdashboardcontroller.md)
  A controller that provides shortcut buttons for the CarPlay Dashboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationdashboardscene/dashboardcontroller)*