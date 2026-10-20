# selectAlternateSetting(_:)

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Selects an alternative setting for the interface.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func selectAlternateSetting(_ alternateSetting: Int) throws
```

```objc
- (BOOL) selectAlternateSetting:(NSUInteger) alternateSetting error:(NSError **) error;
```

#### Discussion

Use this method to select an alternative setting for the interface. The operation aborts all pending input/output requests on the interface’s pipes, and closes all open pipes. It also selects the new alternative setting through the `SET_INTERFACE` control request (See USB 3.2, 9.4.10.).

> **Note**:  Any [`IOUSBHostPipe`](../iousbhostpipe.md) objects that already exist are no longer valid.

## Parameters

- `alternateSetting`: The alternative interface number to activate.

## See Also

### Managing Pipes
- [func copyPipe(withAddress: Int) throws -> IOUSBHostPipe](./copypipe%28withaddress%29.md)
  Copies a pipe for a specific endpoint address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostinterface/selectalternatesetting(_:))*