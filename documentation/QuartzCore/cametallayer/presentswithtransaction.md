# presentsWithTransaction

**Framework**: Core Animation  
**Kind**: property

A Boolean value that determines whether the layer presents its content using a Core Animation transaction.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var presentsWithTransaction: Bool { get set }
```

#### Discussion

By default, this value is [`false`](https://developer.apple.com/documentation/swift/false); [`CAMetalLayer`](cametallayer.md) displays the output of a rendering pass to the display as quickly as possible and asynchronously to any Core Animation transactions. Core Animation doesn’t guarantee that the Metal content arrives in the same frame as other Core Animation content. This behavior could be an issue if, for example, your app draws [`UIKit`](https://developer.apple.comhttps://developer.apple.com/library/archive/releasenotes/General/RN-iOSSDK-6_1/index.html#//apple_ref/doc/uid/TP40012869-CH1-SW17) content over the top of your [`CAMetalLayer`](cametallayer.md).

Setting this value to [`true`](https://developer.apple.com/documentation/swift/true) makes the layer draw its contents synchronously, using whichever Core Animation transaction is current at the time you call the drawable’s [`present()`](https://developer.apple.com/documentation/Metal/MTLDrawable/present()) method. To ensure that a transaction is available when you schedule the drawable to be presented, first commit the command buffer containing your Metal rendering commands. Then, call its [`waitUntilScheduled()`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer/waitUntilScheduled()) method to synchronously wait until the command queue schedules the command buffer to execute on the GPU. Finally, call the drawable’s [`present()`](https://developer.apple.com/documentation/Metal/MTLDrawable/present()) method.

> ⚠️ **Warning**:  If you’re synchronizing presentation with a Core Animation transaction, don’t use the [`present(_:)`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer/present(_:)) method on the command buffer to schedule the drawable for presentation. This convenience method (and any variant of it on [`MTLCommandBuffer`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer)) doesn’t wait for a transaction to be available.

 If you’re synchronizing presentation with a Core Animation transaction, don’t use the [`present(_:)`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer/present(_:)) method on the command buffer to schedule the drawable for presentation. This convenience method (and any variant of it on [`MTLCommandBuffer`](https://developer.apple.com/documentation/Metal/MTLCommandBuffer)) doesn’t wait for a transaction to be available.

## See Also

- [var displaySyncEnabled: Bool](cametallayer/displaysyncenabled.md)
  A Boolean value that determines whether the layer synchronizes its updates to the display’s refresh rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametallayer/presentswithtransaction)*