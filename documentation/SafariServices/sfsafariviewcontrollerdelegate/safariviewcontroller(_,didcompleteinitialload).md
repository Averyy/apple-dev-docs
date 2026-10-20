# safariViewController(_:didCompleteInitialLoad:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the initial URL load completed.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func safariViewController(_ controller: SFSafariViewController, didCompleteInitialLoad didLoadSuccessfully: Bool)
```

```objc
- (void) safariViewController:(SFSafariViewController *) controller didCompleteInitialLoad:(BOOL) didLoadSuccessfully;
```

#### Discussion

This method is invoked when [`SFSafariViewController`](../sfsafariviewcontroller.md) completes the loading of the URL that you pass to its initializer. The method is not invoked for any subsequent page loads in the same [`SFSafariViewController`](../sfsafariviewcontroller.md) instance.

## Parameters

- `controller`: The view controller.
- `didLoadSuccessfully`: [`true`](../../Swift/true.md) if loading completed successfully; otherwise, [`false`](../../Swift/false.md).

## See Also

### Working with the View Controller
- [func safariViewController(SFSafariViewController, activityItemsFor: URL, title: String?) -> [UIActivity]](./safariviewcontroller%28_,activityitemsfor,title%29.md)
  Tells the delegate that the user tapped an Action button.
- [func safariViewControllerDidFinish(SFSafariViewController)](./safariviewcontrollerdidfinish%28_%29.md)
  Tells the delegate that the user dismissed the view.
- [func safariViewController(SFSafariViewController, excludedActivityTypesFor: URL, title: String?) -> [UIActivity.ActivityType]](./safariviewcontroller%28_,excludedactivitytypesfor,title%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontrollerdelegate/safariviewcontroller(_:didcompleteinitialload:))*