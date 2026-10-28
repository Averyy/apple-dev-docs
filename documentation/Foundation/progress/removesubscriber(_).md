# removeSubscriber(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Removes a proxy progress object that the add subscriber method returns.

**Availability**:
- macOS 10.9+

## Declaration

```swift
class func removeSubscriber(_ subscriber: Any)
```

```objc
+ (void) removeSubscriber:(id) subscriber;
```

## Discussion

If the block for [`addSubscriber(forFileURL:withPublishingHandler:)`](./addsubscriber%28forfileurl,withpublishinghandler%29.md) returns a closure, the system invokes that closure on the main thread when you invoke [`removeSubscriber(_:)`](./removesubscriber%28_%29.md).

## Parameters

- `subscriber`: The proxy of the progress object to observe.

## See Also

### Observing and Controlling File Progress by Other Processes
- [class func addSubscriber(forFileURL: URL, withPublishingHandler: Progress.PublishingHandler) -> Any](./addsubscriber%28forfileurl,withpublishinghandler%29.md)
  Registers a file URL to hear about the progress of a file operation.
- [var isOld: Bool](./isold.md)
  A Boolean value that indicates when the observed progress object invokes the publish method before you subscribe to it.
- [typealias PublishingHandler](./publishinghandler.md)
  A block that the system calls when an observed progress object matches the subscription.
- [typealias UnpublishingHandler](./unpublishinghandler.md)
  A block that the system calls when an observed progress object terminates the subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/removesubscriber(_:))*