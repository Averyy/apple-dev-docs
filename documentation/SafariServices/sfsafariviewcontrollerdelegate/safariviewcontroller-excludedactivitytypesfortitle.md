# safariViewController(_:excludedActivityTypesFor:title:)

**Framework**: Safari Services  
**Kind**: method

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func safariViewController(_ controller: SFSafariViewController, excludedActivityTypesFor URL: URL, title: String?) -> [UIActivity.ActivityType]
```

## See Also

- [func safariViewController(SFSafariViewController, didCompleteInitialLoad: Bool)](sfsafariviewcontrollerdelegate/safariviewcontroller(_:didcompleteinitialload:).md)
  Tells the delegate that the initial URL load completed.
- [func safariViewController(SFSafariViewController, activityItemsFor: URL, title: String?) -> [UIActivity]](sfsafariviewcontrollerdelegate/safariviewcontroller(_:activityitemsfor:title:).md)
  Tells the delegate that the user tapped an Action button.
- [func safariViewControllerDidFinish(SFSafariViewController)](sfsafariviewcontrollerdelegate/safariviewcontrollerdidfinish(_:).md)
  Tells the delegate that the user dismissed the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontrollerdelegate/safariviewcontroller(_:excludedactivitytypesfor:title:))*