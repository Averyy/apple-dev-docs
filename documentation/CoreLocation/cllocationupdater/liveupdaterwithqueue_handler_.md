# liveUpdaterWithQueue:handler:

**Framework**: Core Location  
**Kind**: method  
**Role**: Type Method

Creates a location updater on the queue you specify.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
+ (instancetype) liveUpdaterWithQueue:(dispatch_queue_t) queue handler:(void (^)(CLUpdate *update)) handler;
```

#### Return Value

Returns a location updater instance with the specified queue and update handler.

## Parameters

- `queue`: Specifies the queue to which the framework submits the handler with each available update
- `handler`: The block that the framework invokes with each update.

## See Also

### Creating a location updater
- [+ liveUpdaterWithConfiguration:queue:handler:](./liveupdaterwithconfiguration_queue_handler_.md)
  Creates a location updater with the configuration and queue that you specify.
- [CLLiveUpdateConfiguration](../clliveupdateconfiguration.md)
  Specifies the types of locations that a location updater generates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationupdater/liveupdaterwithqueue:handler:)*