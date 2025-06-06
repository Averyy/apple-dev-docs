# commit

**Framework**: HIDDriverKit  
**Kind**: method

Commits the element value to and from the device.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
IOReturn commit(IOHIDElementCommitDirection direction);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

## Parameters

- `direction`: The direction to commit the element. Specify   to read the element data from the device. Specify   to write the element data to the device.

## See Also

- [IOHIDElementCommitDirection](iohidelementcommitdirection.md)
  The commit direction for an HID element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidelement/commit)*