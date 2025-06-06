# applicationSignificantTimeChange(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate when there is a significant change in the time.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func applicationSignificantTimeChange(_ application: UIApplication)
```

#### Discussion

Examples of significant time changes include the arrival of midnight, an update of the time by a carrier, and the change to daylight savings time. The delegate can implement this method to adjust any object of the app that displays time or is sensitive to time changes.

Prior to calling this method, the app also posts a [`significantTimeChangeNotification`](uiapplication/significanttimechangenotification.md) notification to give interested objects a chance to respond to the change.

If your app is currently suspended, this message is queued until your app returns to the foreground, at which point it is delivered. If multiple time changes occur, only the most recent one is delivered.

## Parameters

- `application`: Your singleton app object.

## See Also

- [func applicationProtectedDataDidBecomeAvailable(UIApplication)](uiapplicationdelegate/applicationprotecteddatadidbecomeavailable(_:).md)
  Tells the delegate that protected files are available now.
- [func applicationProtectedDataWillBecomeUnavailable(UIApplication)](uiapplicationdelegate/applicationprotecteddatawillbecomeunavailable(_:).md)
  Tells the delegate that the protected files are about to become unavailable.
- [func applicationDidReceiveMemoryWarning(UIApplication)](uiapplicationdelegate/applicationdidreceivememorywarning(_:).md)
  Tells the delegate when the app receives a memory warning from the system.
- [class let protectedDataDidBecomeAvailableNotification: NSNotification.Name](uiapplication/protecteddatadidbecomeavailablenotification.md)
  A notification that posts when the protected files become available for your code to access.
- [class let protectedDataWillBecomeUnavailableNotification: NSNotification.Name](uiapplication/protecteddatawillbecomeunavailablenotification.md)
  A notification that posts shortly before protected files are locked down and become inaccessible.
- [class let didReceiveMemoryWarningNotification: NSNotification.Name](uiapplication/didreceivememorywarningnotification.md)
  A notification that posts when the app receives a warning from the operating system about low memory availability.
- [class let significantTimeChangeNotification: NSNotification.Name](uiapplication/significanttimechangenotification.md)
  A notification that posts when there’s a significant change in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationsignificanttimechange(_:))*