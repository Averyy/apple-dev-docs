# kIOHIDElementCommitDirectionOut

**Framework**: HIDDriverKit  
**Kind**: case

Causes the element data to be sent to the device.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
kIOHIDElementCommitDirectionOut
```

#### Discussion

Specifying this direction causes the [`commit`](iohidelement/commit.md) function to send the element data to the device. Use the [`setValue`](iohidelement/setvalue.md) or [`setDataValue`](iohidelement/setdatavalue.md) functions to specify the new data before committing it.

## See Also

- [kIOHIDElementCommitDirectionIn](iohidelementcommitdirection/kiohidelementcommitdirectionin.md)
  Causes the retrieval of information from the device, and the populating of the element with the resulting data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidelementcommitdirection/kiohidelementcommitdirectionout)*