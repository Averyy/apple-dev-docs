# removeSubscriber(_:)

**Framework**: Foundation  
**Kind**: method

Removes a proxy progress object that the add subscriber method returns.

**Availability**:
- macOS 10.9+

## Declaration

```swift
class func removeSubscriber(_ subscriber: Any)
```

#### Discussion

If the block for [`addSubscriber(forFileURL:withPublishingHandler:)`](progress/addsubscriber(forfileurl:withpublishinghandler:).md) returns a closure, the system invokes that closure on the main thread when you invoke [`removeSubscriber(_:)`](progress/removesubscriber(_:).md).

## Parameters

- `subscriber`: The proxy of the progress object to observe.

## See Also

- [class func addSubscriber(forFileURL: URL, withPublishingHandler: Progress.PublishingHandler) -> Any](progress/addsubscriber(forfileurl:withpublishinghandler:).md)
  Registers a file URL to hear about the progress of a file operation.
- [var isOld: Bool](progress/isold.md)
  A Boolean value that indicates when the observed progress object invokes the publish method before you subscribe to it.
- [typealias PublishingHandler](progress/publishinghandler.md)
  A block that the system calls when an observed progress object matches the subscription.
- [typealias UnpublishingHandler](progress/unpublishinghandler.md)
  A block that the system calls when an observed progress object terminates the subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/removesubscriber(_:))*