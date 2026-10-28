# safariViewController(_:activityItemsFor:title:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user tapped an Action button.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func safariViewController(_ controller: SFSafariViewController, activityItemsFor URL: URL, title: String?) -> [UIActivity]
```

```objc
- (NSArray<UIActivity *> *) safariViewController:(SFSafariViewController *) controller activityItemsForURL:(NSURL *) URL title:(NSString *) title;
```

## Return Value

An array of application-specific services you have chosen to include in the [`UIActivityViewController`](../../UIKit/uiactivityviewcontroller.md) object.

## Discussion

The view controller calls this method when the view is about to show an activity view controller. Your delegate can provide unique, application-specific services (such as a social media service) to be included with the system-provided sharing services. See [`UIActivity`](../../UIKit/uiactivity.md).

## Parameters

- `controller`: The view controller.
- `URL`: The URL of the web page that was active when the Action button was tapped.
- `title`: The title of the web page.

## See Also

### Working with the View Controller
- [func safariViewController(SFSafariViewController, didCompleteInitialLoad: Bool)](./safariviewcontroller%28_,didcompleteinitialload%29.md)
  Tells the delegate that the initial URL load completed.
- [func safariViewControllerDidFinish(SFSafariViewController)](./safariviewcontrollerdidfinish%28_%29.md)
  Tells the delegate that the user dismissed the view.
- [func safariViewController(SFSafariViewController, excludedActivityTypesFor: URL, title: String?) -> [UIActivity.ActivityType]](./safariviewcontroller%28_,excludedactivitytypesfor,title%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontrollerdelegate/safariviewcontroller(_:activityitemsfor:title:))*