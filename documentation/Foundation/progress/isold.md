# isOld

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates when the observed progress object invokes the publish method before you subscribe to it.

**Availability**:
- macOS 10.9+

## Declaration

```swift
var isOld: Bool { get }
```

```objc
@property (readonly, getter=isOld) BOOL old;
```

#### Discussion

The publish and subscribe mechanism is generally *level-triggered*, in that when you invoke [`addSubscriber(forFileURL:withPublishingHandler:)`](./addsubscriber%28forfileurl,withpublishinghandler%29.md), the system invokes your block for every relevant published and unpublished progress object. Sometimes you need to implement *edge-triggered* behavior, in which you do something either exactly when new progress begins or not at all.

In the example above, the Dock doesn’t animate file icons when this method returns [`true`](../../Swift/true.md).

There’s no reliable definition of *before* in this case, which involves multiple processes in a preemptively scheduled system. Don’t use this method for anything more important than best efforts at animating. It can be inaccurate due to processes coming and going from unpredictable user actions.

## See Also

### Observing and Controlling File Progress by Other Processes
- [class func addSubscriber(forFileURL: URL, withPublishingHandler: Progress.PublishingHandler) -> Any](./addsubscriber%28forfileurl,withpublishinghandler%29.md)
  Registers a file URL to hear about the progress of a file operation.
- [class func removeSubscriber(Any)](./removesubscriber%28_%29.md)
  Removes a proxy progress object that the add subscriber method returns.
- [typealias PublishingHandler](./publishinghandler.md)
  A block that the system calls when an observed progress object matches the subscription.
- [typealias UnpublishingHandler](./unpublishinghandler.md)
  A block that the system calls when an observed progress object terminates the subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/isold)*