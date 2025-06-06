# safariViewController(_:didCompleteInitialLoad:)

**Framework**: Safari Services  
**Kind**: method

Tells the delegate that the initial URL load completed.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func safariViewController(_ controller: SFSafariViewController, didCompleteInitialLoad didLoadSuccessfully: Bool)
```

#### Discussion

This method is invoked when [`SFSafariViewController`](sfsafariviewcontroller.md) completes the loading of the URL that you pass to its initializer. The method is not invoked for any subsequent page loads in the same [`SFSafariViewController`](sfsafariviewcontroller.md) instance.

## Parameters

- `controller`: The view controller.
- `didLoadSuccessfully`:   if loading completed successfully; otherwise,  .

## See Also

- [func safariViewController(SFSafariViewController, activityItemsFor: URL, title: String?) -> [UIActivity]](sfsafariviewcontrollerdelegate/safariviewcontroller(_:activityitemsfor:title:).md)
  Tells the delegate that the user tapped an Action button.
- [func safariViewControllerDidFinish(SFSafariViewController)](sfsafariviewcontrollerdelegate/safariviewcontrollerdidfinish(_:).md)
  Tells the delegate that the user dismissed the view.
- [func safariViewController(SFSafariViewController, excludedActivityTypesFor: URL, title: String?) -> [UIActivity.ActivityType]](sfsafariviewcontrollerdelegate/safariviewcontroller(_:excludedactivitytypesfor:title:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontrollerdelegate/safariviewcontroller(_:didcompleteinitialload:))*