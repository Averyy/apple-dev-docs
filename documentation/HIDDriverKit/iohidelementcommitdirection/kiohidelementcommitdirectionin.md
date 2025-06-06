# kIOHIDElementCommitDirectionIn

**Framework**: HIDDriverKit  
**Kind**: case

Causes the retrieval of information from the device, and the populating of the element with the resulting data.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
kIOHIDElementCommitDirectionIn
```

#### Discussion

Specifying this direction causes the [`commit`](iohidelement/commit.md) function to read the element data from the device and update the current object. You can access the resulting data using the [`getValue`](iohidelement/getvalue.md) or [`getDataValue`](iohidelement/getdatavalue.md) functions.

## See Also

- [kIOHIDElementCommitDirectionOut](iohidelementcommitdirection/kiohidelementcommitdirectionout.md)
  Causes the element data to be sent to the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidelementcommitdirection/kiohidelementcommitdirectionin)*