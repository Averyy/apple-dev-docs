# Progress.PublishingHandler

**Framework**: Foundation  
**Kind**: typealias  
**Role**: Type Alias

A block that the system calls when an observed progress object matches the subscription.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
typealias PublishingHandler = @Sendable (Progress) -> Progress.UnpublishingHandler?
```

```c
typedef void (^(^)(NSProgress *))(void) NSProgressPublishingHandler;
```

#### Return Value

An optional block that the system invokes when the observed progress object invokes [`unpublish()`](./unpublish%28%29.md), the publishing process terminates, or you invoke [`removeSubscriber(_:)`](./removesubscriber%28_%29.md).

## Parameters

- `progress`: The proxy to the observed progress object.

## See Also

### Observing and Controlling File Progress by Other Processes
- [class func addSubscriber(forFileURL: URL, withPublishingHandler: Progress.PublishingHandler) -> Any](./addsubscriber%28forfileurl,withpublishinghandler%29.md)
  Registers a file URL to hear about the progress of a file operation.
- [class func removeSubscriber(Any)](./removesubscriber%28_%29.md)
  Removes a proxy progress object that the add subscriber method returns.
- [var isOld: Bool](./isold.md)
  A Boolean value that indicates when the observed progress object invokes the publish method before you subscribe to it.
- [typealias UnpublishingHandler](./unpublishinghandler.md)
  A block that the system calls when an observed progress object terminates the subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/publishinghandler)*