# addSubscriber(forFileURL:withPublishingHandler:)

**Framework**: Foundation  
**Kind**: method

Registers a file URL to hear about the progress of a file operation.

**Availability**:
- macOS 10.9+

## Declaration

```swift
class func addSubscriber(forFileURL url: URL, withPublishingHandler publishingHandler: @escaping Progress.PublishingHandler) -> Any
```

#### Return Value

A proxy of the progress object to observe.

#### Discussion

The system invokes the passed-in block when a progress object calls [`publish()`](progress/publish().md) with a [`fileURLKey`](progressuserinfokey/fileurlkey.md) user info dictionary entry that’s a URL that is the same as this method’s URL, or that is an item that the URL directly contains. The progress object that passes to your block is a proxy of the published progress object. The passed-in block may return another block. If it does, the system invokes the returned block when the observed progress object invokes [`unpublish()`](progress/unpublish().md), the publishing process terminates, or you invoke [`removeSubscriber(_:)`](progress/removesubscriber(_:).md). The system invokes the blocks you provide on the main thread.

## Parameters

- `url`: The URL of the file to observe.
- `publishingHandler`: A closure that the system invokes when a progress object that represents a file operation matching the specified URL calls  .

## See Also

- [class func removeSubscriber(Any)](progress/removesubscriber(_:).md)
  Removes a proxy progress object that the add subscriber method returns.
- [var isOld: Bool](progress/isold.md)
  A Boolean value that indicates when the observed progress object invokes the publish method before you subscribe to it.
- [typealias PublishingHandler](progress/publishinghandler.md)
  A block that the system calls when an observed progress object matches the subscription.
- [typealias UnpublishingHandler](progress/unpublishinghandler.md)
  A block that the system calls when an observed progress object terminates the subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/addsubscriber(forfileurl:withpublishinghandler:))*