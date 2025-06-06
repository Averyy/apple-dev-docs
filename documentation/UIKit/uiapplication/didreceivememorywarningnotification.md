# didReceiveMemoryWarningNotification

**Framework**: UIKit  
**Kind**: property

A notification that posts when the app receives a warning from the operating system about low memory availability.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
nonisolated
class let didReceiveMemoryWarningNotification: NSNotification.Name
```

## Mentions

- [Responding to memory warnings](responding-to-memory-warnings.md)

#### Discussion

This notification does not contain a `userInfo` dictionary.

## See Also

- [func applicationProtectedDataDidBecomeAvailable(UIApplication)](uiapplicationdelegate/applicationprotecteddatadidbecomeavailable(_:).md)
  Tells the delegate that protected files are available now.
- [func applicationProtectedDataWillBecomeUnavailable(UIApplication)](uiapplicationdelegate/applicationprotecteddatawillbecomeunavailable(_:).md)
  Tells the delegate that the protected files are about to become unavailable.
- [func applicationDidReceiveMemoryWarning(UIApplication)](uiapplicationdelegate/applicationdidreceivememorywarning(_:).md)
  Tells the delegate when the app receives a memory warning from the system.
- [func applicationSignificantTimeChange(UIApplication)](uiapplicationdelegate/applicationsignificanttimechange(_:).md)
  Tells the delegate when there is a significant change in the time.
- [class let protectedDataDidBecomeAvailableNotification: NSNotification.Name](uiapplication/protecteddatadidbecomeavailablenotification.md)
  A notification that posts when the protected files become available for your code to access.
- [class let protectedDataWillBecomeUnavailableNotification: NSNotification.Name](uiapplication/protecteddatawillbecomeunavailablenotification.md)
  A notification that posts shortly before protected files are locked down and become inaccessible.
- [class let significantTimeChangeNotification: NSNotification.Name](uiapplication/significanttimechangenotification.md)
  A notification that posts when there’s a significant change in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/didreceivememorywarningnotification)*