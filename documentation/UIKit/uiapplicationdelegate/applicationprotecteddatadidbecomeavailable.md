# applicationProtectedDataDidBecomeAvailable(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that protected files are available now.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func applicationProtectedDataDidBecomeAvailable(_ application: UIApplication)
```

## Mentions

- [Encrypting Your App’s Files](encrypting-your-app-s-files.md)

#### Discussion

On a device that uses content protection, protected files are stored in an encrypted form and made available only at certain times, usually when the device is unlocked. This notification lets your app know that the device is now unlocked and that you may access certain types of protected files again.

## Parameters

- `application`: Your singleton app object.

## See Also

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
- [class let didReceiveMemoryWarningNotification: NSNotification.Name](uiapplication/didreceivememorywarningnotification.md)
  A notification that posts when the app receives a warning from the operating system about low memory availability.
- [class let significantTimeChangeNotification: NSNotification.Name](uiapplication/significanttimechangenotification.md)
  A notification that posts when there’s a significant change in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationprotecteddatadidbecomeavailable(_:))*