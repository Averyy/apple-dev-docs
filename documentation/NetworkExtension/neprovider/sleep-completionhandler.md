# sleep(completionHandler:)

**Framework**: Network Extension  
**Kind**: method

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
func sleep() async
```

#### Discussion

This method is called by the system when the device is about to go to sleep.

`NEProvider` subclasses should override this method if the provider needs to perform any tasks before the device sleeps, such as disconnecting a tunnel connection.

## Parameters

- `completionHandler`: Implementations of this method must execute this block when the provider is finished handling the sleep event.

## See Also

- [func wake()](neprovider/wake.md)
  Handle a wake event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neprovider/sleep(completionhandler:))*