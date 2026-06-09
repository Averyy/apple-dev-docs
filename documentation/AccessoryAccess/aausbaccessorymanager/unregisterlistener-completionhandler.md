# unregisterListener(_:completionHandler:)

**Framework**: Accessory Access  
**Kind**: method

Unregister a previously registered listener.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func unregisterListener(_ listener: any AAUSBAccessoryListener) async
```

## Parameters

- `listener`: The listener of USB accessories.
- `completionHandler`: The block the framework calls after it successfully unregisters the listener. The framework invokes the block on an arbitrary thread.

## See Also

- [func registerListener(any AAUSBAccessoryListener, matchingCriteria: [AAUSBAccessoryMatchingCriteria], completionHandler: ([AAUSBAccessory], (any Error)?) -> Void)](aausbaccessorymanager/registerlistener(_:matchingcriteria:completionhandler:).md)
  Registers a USB accessory listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorymanager/unregisterlistener(_:completionhandler:))*