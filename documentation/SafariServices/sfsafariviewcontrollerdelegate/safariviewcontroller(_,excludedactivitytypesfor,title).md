# safariViewController(_:excludedActivityTypesFor:title:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func safariViewController(_ controller: SFSafariViewController, excludedActivityTypesFor URL: URL, title: String?) -> [UIActivity.ActivityType]
```

```objc
- (NSArray<NSString *> *) safariViewController:(SFSafariViewController *) controller excludedActivityTypesForURL:(NSURL *) URL title:(NSString *) title;
```

## See Also

### Working with the View Controller
- [func safariViewController(SFSafariViewController, didCompleteInitialLoad: Bool)](./safariviewcontroller%28_,didcompleteinitialload%29.md)
  Tells the delegate that the initial URL load completed.
- [func safariViewController(SFSafariViewController, activityItemsFor: URL, title: String?) -> [UIActivity]](./safariviewcontroller%28_,activityitemsfor,title%29.md)
  Tells the delegate that the user tapped an Action button.
- [func safariViewControllerDidFinish(SFSafariViewController)](./safariviewcontrollerdidfinish%28_%29.md)
  Tells the delegate that the user dismissed the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontrollerdelegate/safariviewcontroller(_:excludedactivitytypesfor:title:))*