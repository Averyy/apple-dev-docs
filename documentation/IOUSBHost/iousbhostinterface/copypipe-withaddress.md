# copyPipe(withAddress:)

**Framework**: IOUSBHost  
**Kind**: method

Copies a pipe for a specific endpoint address.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func copyPipe(withAddress address: Int) throws -> IOUSBHostPipe
```

#### Return Value

An [`IOUSBHostPipe`](iousbhostpipe.md) or [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) if the system can’t create the pipe.

#### Discussion

If the pipe returns successfully, the method maintains a reference to the [`IOUSBHostInterface`](iousbhostinterface.md).

## Parameters

- `address`: The endpoint address of the pipe.

## See Also

- [func selectAlternateSetting(Int) throws](iousbhostinterface/selectalternatesetting(_:).md)
  Selects an alternative setting for the interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostinterface/copypipe(withaddress:))*