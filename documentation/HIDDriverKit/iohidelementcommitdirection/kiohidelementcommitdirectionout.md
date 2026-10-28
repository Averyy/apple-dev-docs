# kIOHIDElementCommitDirectionOut

**Framework**: HIDDriverKit  
**Kind**: case  
**Role**: Enumeration Case

Causes the element data to be sent to the device.

**Availability**:
- DriverKit
- macOS

## Declaration

```c
kIOHIDElementCommitDirectionOut
```

## Discussion

Specifying this direction causes the [`commit`](../iohidelement/commit.md) function to send the element data to the device. Use the [`setValue`](../iohidelement/setvalue.md) or [`setDataValue`](../iohidelement/setdatavalue.md) functions to specify the new data before committing it.

## See Also

### Getting the Commit Directions
- [kIOHIDElementCommitDirectionIn](./kiohidelementcommitdirectionin.md)
  Causes the retrieval of information from the device, and the populating of the element with the resulting data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidelementcommitdirection/kiohidelementcommitdirectionout)*