# sleep(completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Handle a sleep event.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func sleep(completionHandler: @escaping @Sendable () -> Void)
```

```swift
func sleep() async
```

```objc
- (void) sleepWithCompletionHandler:(void (^)()) completionHandler;
```

## Discussion

This method is called by the system when the device is about to go to sleep.

`NEProvider` subclasses should override this method if the provider needs to perform any tasks before the device sleeps, such as disconnecting a tunnel connection.

## Parameters

- `completionHandler`: Implementations of this method must execute this block when the provider is finished handling the sleep event.

## See Also

### Handling sleep and wake
- [func wake()](./wake%28%29.md)
  Handle a wake event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neprovider/sleep(completionhandler:))*