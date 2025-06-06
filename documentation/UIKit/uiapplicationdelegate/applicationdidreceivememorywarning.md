# applicationDidReceiveMemoryWarning(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate when the app receives a memory warning from the system.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func applicationDidReceiveMemoryWarning(_ application: UIApplication)
```

## Mentions

- [Responding to memory warnings](responding-to-memory-warnings.md)

#### Discussion

Your implementation of this method should free up as much memory as possible by purging cached data objects that can be recreated (or reloaded from disk) later. You use this method in conjunction with the [`didReceiveMemoryWarning()`](uiviewcontroller/didreceivememorywarning().md) of the [`UIViewController`](uiviewcontroller.md) class and the [`didReceiveMemoryWarningNotification`](uiapplication/didreceivememorywarningnotification.md) notification to release memory throughout your app.

It is strongly recommended that you implement this method. If your app does not release enough memory during low-memory conditions, the system may terminate it outright.

## Parameters

- `application`: Your singleton app object.

## See Also

- [func didReceiveMemoryWarning()](uiviewcontroller/didreceivememorywarning.md)
  Sent to the view controller when the app receives a memory warning.
- [func applicationProtectedDataDidBecomeAvailable(UIApplication)](uiapplicationdelegate/applicationprotecteddatadidbecomeavailable(_:).md)
  Tells the delegate that protected files are available now.
- [func applicationProtectedDataWillBecomeUnavailable(UIApplication)](uiapplicationdelegate/applicationprotecteddatawillbecomeunavailable(_:).md)
  Tells the delegate that the protected files are about to become unavailable.
- [func applicationSignificantTimeChange(UIApplication)](uiapplicationdelegate/applicationsignificanttimechange(_:).md)
  Tells the delegate when there is a significant change in the time.
- [class let protectedDataDidBecomeAvailableNotification: NSNotification.Name](uiapplication/protecteddatadidbecomeavailablenotification.md)
  A notification that posts when the protected files become available for your code to access.
- [class let protectedDataWillBecomeUnavailableNotification: NSNotification.Name](uiapplication/protecteddatawillbecomeunavailablenotification.md)
  A notification that posts shortly before protected files are locked down and become inaccessible.
- [class let didReceiveMemoryWarningNotification: NSNotification.Name](uiapplication/didreceivememorywarningnotification.md)
  A notification that posts when the app receives a warning from the operating system about low memory availability.
- [class let significantTimeChangeNotification: NSNotification.Name](uiapplication/significanttimechangenotification.md)
  A notification that posts when there’s a significant change in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationdidreceivememorywarning(_:))*