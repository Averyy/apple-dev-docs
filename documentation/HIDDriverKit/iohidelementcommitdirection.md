# IOHIDElementCommitDirection

**Framework**: HIDDriverKit  
**Kind**: enum

The commit direction for an HID element.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
typedef enum { ... } IOHIDElementCommitDirection;
```

#### Overview

Passing a value of [`kIOHIDElementCommitDirectionOut`](iohidelementcommitdirection/kiohidelementcommitdirectionout.md) issues a [`setReport`](iohiddevice/setreport.md) call to the device. Before issuing this call, set your desired value on the element with the [`setValue`](iohidelement/setvalue.md) or [`setDataValue`](iohidelement/setdatavalue.md) functions.

## Topics

### Getting the Commit Directions
- [kIOHIDElementCommitDirectionIn](iohidelementcommitdirection/kiohidelementcommitdirectionin.md)
  Causes the retrieval of information from the device, and the populating of the element with the resulting data.
- [kIOHIDElementCommitDirectionOut](iohidelementcommitdirection/kiohidelementcommitdirectionout.md)
  Causes the element data to be sent to the device.

## See Also

- [commit](iohidelement/commit.md)
  Commits the element value to and from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidelementcommitdirection)*