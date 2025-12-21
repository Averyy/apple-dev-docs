# isOld

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates when the observed progress object invokes the publish method before you subscribe to it.

**Availability**:
- macOS 10.9+

## Declaration

```swift
var isOld: Bool { get }
```

#### Discussion

The publish and subscribe mechanism is generally , in that when you invoke [`addSubscriber(forFileURL:withPublishingHandler:)`](progress/addsubscriber(forfileurl:withpublishinghandler:).md), the system invokes your block for every relevant published and unpublished progress object. Sometimes you need to implement  behavior, in which you do something either exactly when new progress begins or not at all.

In the example above, the Dock doesn’t animate file icons when this method returns [`true`](https://developer.apple.com/documentation/Swift/true).

There’s no reliable definition of  in this case, which involves multiple processes in a preemptively scheduled system. Don’t use this method for anything more important than best efforts at animating. It can be inaccurate due to processes coming and going from unpredictable user actions.

## See Also

- [class func addSubscriber(forFileURL: URL, withPublishingHandler: Progress.PublishingHandler) -> Any](progress/addsubscriber(forfileurl:withpublishinghandler:).md)
  Registers a file URL to hear about the progress of a file operation.
- [class func removeSubscriber(Any)](progress/removesubscriber(_:).md)
  Removes a proxy progress object that the add subscriber method returns.
- [typealias PublishingHandler](progress/publishinghandler.md)
  A block that the system calls when an observed progress object matches the subscription.
- [typealias UnpublishingHandler](progress/unpublishinghandler.md)
  A block that the system calls when an observed progress object terminates the subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/isold)*