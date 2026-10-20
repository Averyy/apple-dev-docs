# unregisterListener(_:completionHandler:)

**Framework**: Accessory Access  
**Kind**: method  
**Role**: Instance Method

Unregister a previously registered listener.

**Availability**:
- macOS 27.0+

## Declaration

```swift
func unregisterListener(_ listener: any AAUSBAccessoryListener, completionHandler: @escaping @Sendable () -> Void)
```

```swift
func unregisterListener(_ listener: any AAUSBAccessoryListener) async
```

```objc
- (void) unregisterListener:(id<AAUSBAccessoryListener>) listener completionHandler:(void (^)()) completionHandler;
```

## Parameters

- `listener`: The listener of USB accessories.
- `completionHandler`: The block the framework calls after it successfully unregisters the listener. The framework invokes the block on an arbitrary thread.

## See Also

### Registering and unregistering listeners
- [func registerListener(any AAUSBAccessoryListener, matchingCriteria: [AAUSBAccessoryMatchingCriteria], completionHandler: ([AAUSBAccessory], (any Error)?) -> Void)](./registerlistener%28_,matchingcriteria,completionhandler%29.md)
  Registers a USB accessory listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorymanager/unregisterlistener(_:completionhandler:))*