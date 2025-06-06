# safariViewController(_:activityItemsFor:title:)

**Framework**: Safari Services  
**Kind**: method

Tells the delegate that the user tapped an Action button.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func safariViewController(_ controller: SFSafariViewController, activityItemsFor URL: URL, title: String?) -> [UIActivity]
```

#### Return Value

An array of application-specific services you have chosen to include in the [`UIActivityViewController`](https://developer.apple.com/documentation/UIKit/UIActivityViewController) object.

#### Discussion

The view controller calls this method when the view is about to show an activity view controller. Your delegate can provide unique, application-specific services (such as a social media service) to be included with the system-provided sharing services. See [`UIActivity`](https://developer.apple.com/documentation/UIKit/UIActivity).

## Parameters

- `controller`: The view controller.
- `URL`: The URL of the web page that was active when the Action button was tapped.
- `title`: The title of the web page.

## See Also

- [func safariViewController(SFSafariViewController, didCompleteInitialLoad: Bool)](sfsafariviewcontrollerdelegate/safariviewcontroller(_:didcompleteinitialload:).md)
  Tells the delegate that the initial URL load completed.
- [func safariViewControllerDidFinish(SFSafariViewController)](sfsafariviewcontrollerdelegate/safariviewcontrollerdidfinish(_:).md)
  Tells the delegate that the user dismissed the view.
- [func safariViewController(SFSafariViewController, excludedActivityTypesFor: URL, title: String?) -> [UIActivity.ActivityType]](sfsafariviewcontrollerdelegate/safariviewcontroller(_:excludedactivitytypesfor:title:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontrollerdelegate/safariviewcontroller(_:activityitemsfor:title:))*