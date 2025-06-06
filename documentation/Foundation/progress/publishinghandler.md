# Progress.PublishingHandler

**Framework**: Foundation  
**Kind**: typealias

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
typealias PublishingHandler = (Progress) -> Progress.UnpublishingHandler?
```

#### Return Value

An optional block that the system invokes when the observed progress object invokes [`unpublish()`](progress/unpublish().md), the publishing process terminates, or you invoke [`removeSubscriber(_:)`](progress/removesubscriber(_:).md).

## Parameters

- `progress`: The proxy to the observed progress object.

## See Also

- [class func addSubscriber(forFileURL: URL, withPublishingHandler: Progress.PublishingHandler) -> Any](progress/addsubscriber(forfileurl:withpublishinghandler:).md)
  Registers a file URL to hear about the progress of a file operation.
- [class func removeSubscriber(Any)](progress/removesubscriber(_:).md)
  Removes a proxy progress object that the add subscriber method returns.
- [var isOld: Bool](progress/isold.md)
  A Boolean value that indicates when the observed progress object invokes the publish method before you subscribe to it.
- [typealias UnpublishingHandler](progress/unpublishinghandler.md)
  A block that the system calls when an observed progress object terminates the subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/publishinghandler)*