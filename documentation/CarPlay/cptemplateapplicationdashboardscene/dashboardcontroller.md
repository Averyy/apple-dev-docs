# dashboardController

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The controller that manages the dashboard scene’s shortcut buttons.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
var dashboardController: CPDashboardController { get }
```

```objc
@property (nonatomic, strong, readonly, nonnull) CPDashboardController * dashboardController;
```

#### Discussion

Use this property to access the controller CarPlay creates when it connects your navigation app’s dashboard scene. You use this controller to manage the shortcut buttons CarPlay displays in the dashboard when there’s no active navigation session.

## See Also

### Accessing the Dashboard Controller
- [class CPDashboardController](../cpdashboardcontroller.md)
  A controller that provides shortcut buttons for the CarPlay Dashboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationdashboardscene/dashboardcontroller)*