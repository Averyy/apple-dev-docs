# safariViewControllerDidFinish(_:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user dismissed the view.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func safariViewControllerDidFinish(_ controller: SFSafariViewController)
```

```objc
- (void) safariViewControllerDidFinish:(SFSafariViewController *) controller;
```

## Discussion

You can perform any necessary cleanup here. The view controller is dismissed afterwards.

## Parameters

- `controller`: The view controller.

## See Also

### Working with the View Controller
- [func safariViewController(SFSafariViewController, didCompleteInitialLoad: Bool)](./safariviewcontroller%28_,didcompleteinitialload%29.md)
  Tells the delegate that the initial URL load completed.
- [func safariViewController(SFSafariViewController, activityItemsFor: URL, title: String?) -> [UIActivity]](./safariviewcontroller%28_,activityitemsfor,title%29.md)
  Tells the delegate that the user tapped an Action button.
- [func safariViewController(SFSafariViewController, excludedActivityTypesFor: URL, title: String?) -> [UIActivity.ActivityType]](./safariviewcontroller%28_,excludedactivitytypesfor,title%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontrollerdelegate/safariviewcontrollerdidfinish(_:))*