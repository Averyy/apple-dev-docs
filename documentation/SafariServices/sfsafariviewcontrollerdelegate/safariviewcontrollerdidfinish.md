# safariViewControllerDidFinish(_:)

**Framework**: Safari Services  
**Kind**: method

Tells the delegate that the user dismissed the view.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func safariViewControllerDidFinish(_ controller: SFSafariViewController)
```

#### Discussion

You can perform any necessary cleanup here. The view controller is dismissed afterwards.

## Parameters

- `controller`: The view controller.

## See Also

- [func safariViewController(SFSafariViewController, didCompleteInitialLoad: Bool)](sfsafariviewcontrollerdelegate/safariviewcontroller(_:didcompleteinitialload:).md)
  Tells the delegate that the initial URL load completed.
- [func safariViewController(SFSafariViewController, activityItemsFor: URL, title: String?) -> [UIActivity]](sfsafariviewcontrollerdelegate/safariviewcontroller(_:activityitemsfor:title:).md)
  Tells the delegate that the user tapped an Action button.
- [func safariViewController(SFSafariViewController, excludedActivityTypesFor: URL, title: String?) -> [UIActivity.ActivityType]](sfsafariviewcontrollerdelegate/safariviewcontroller(_:excludedactivitytypesfor:title:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontrollerdelegate/safariviewcontrollerdidfinish(_:))*