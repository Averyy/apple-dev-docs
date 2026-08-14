# commitElements

**Framework**: HIDDriverKit  
**Kind**: method

Gets or sets the contents of the interface’s stored elements.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
virtual kern_return_t commitElements(OSArray *elements, IOHIDElementCommitDirection direction);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/driverkit/error-codes).

## Parameters

- `elements`: An array of [`IOHIDElement`](iohidelement.md) objects.
- `direction`: The direction in which to commit changes. Specify [`kIOHIDElementCommitDirectionIn`](iohidelementcommitdirection/kiohidelementcommitdirectionin.md) to read the element data from the device. Specify [`kIOHIDElementCommitDirectionOut`](iohidelementcommitdirection/kiohidelementcommitdirectionout.md) to write the element data to the device.

## See Also

- [getElements](iohidinterface/getelements.md)
  Returns the array of elements that the interface uses to store  parsed report data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidinterface/commitelements)*