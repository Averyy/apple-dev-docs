# selectAlternateSetting(_:)

**Framework**: Iousbhost  
**Kind**: method

Selects an alternative setting for the interface.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func selectAlternateSetting(_ alternateSetting: Int) throws
```

#### Discussion

Use this method to select an alternative setting for the interface. The operation aborts all pending input/output requests on the interface’s pipes, and closes all open pipes. It also selects the new alternative setting through the `SET_INTERFACE` control request (See USB 3.2, 9.4.10.).

> **Note**:  Any [`IOUSBHostPipe`](iousbhostpipe.md) objects that already exist are no longer valid.

## Parameters

- `alternateSetting`: The alternative interface number to activate.

## See Also

- [func copyPipe(withAddress: Int) throws -> IOUSBHostPipe](iousbhostinterface/copypipe(withaddress:).md)
  Copies a pipe for a specific endpoint address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostinterface/selectalternatesetting(_:))*