# registerListener(_:matchingCriteria:completionHandler:)

**Framework**: Accessory Access  
**Kind**: method

Registers a USB accessory listener.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func registerListener(_ listener: any AAUSBAccessoryListener, matchingCriteria: [AAUSBAccessoryMatchingCriteria]) async throws -> [AAUSBAccessory]
```

#### Discussion

Register a  USB accessory listener that satisfies one of the given criteria. The listener is notified when a USB accessory, that satisfies the criteria, connects to or disconnects from the system.

If the listener is already registered, this operation will fail with the AAErrorCodeAccessoryListenerAlreadyRegistered error.

If any accessories matching the criteria are already connected, they are passed to the completion handler.

## Parameters

- `listener`: The USB accessory listener.
- `matchingCriteria`: Matching criteria for filtering USB accessories. [`AAUSBAccessoryManager`](aausbaccessorymanager.md) notifies the listener of USB accessory events if the accessory satisfies any of the [`AAUSBAccessoryMatchingCriteria`](aausbaccessorymatchingcriteria.md)  objects. Passing an empty array matches any USB accessory.
- `completionHandler`: The block the framework calls after it successfully registers the listener. The first parameter passed to the block is an array containing accessories that are already connected and match the provided criteria. The array is empty if there are none. The second parameter passed to the block is `nil` if the framework successfully registered the listener. The block the framework invokes is on an arbitrary thread.

## See Also

- [func unregisterListener(any AAUSBAccessoryListener, completionHandler: () -> Void)](aausbaccessorymanager/unregisterlistener(_:completionhandler:).md)
  Unregister a previously registered listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorymanager/registerlistener(_:matchingcriteria:completionhandler:))*