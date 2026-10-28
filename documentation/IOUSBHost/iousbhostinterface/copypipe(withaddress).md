# copyPipe(withAddress:)

**Framework**: IOUSBHost  
**Kind**: method  
**Role**: Instance Method

Copies a pipe for a specific endpoint address.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func copyPipe(withAddress address: Int) throws -> IOUSBHostPipe
```

```objc
- (IOUSBHostPipe *) copyPipeWithAddress:(NSUInteger) address error:(NSError **) error;
```

## Return Value

An [`IOUSBHostPipe`](../iousbhostpipe.md) or [`nil`](../../ObjectiveC/nil-227m0.md) if the system can’t create the pipe.

## Discussion

If the pipe returns successfully, the method maintains a reference to the [`IOUSBHostInterface`](../iousbhostinterface.md).

## Parameters

- `address`: The endpoint address of the pipe.

## See Also

### Managing Pipes
- [func selectAlternateSetting(Int) throws](./selectalternatesetting%28_%29.md)
  Selects an alternative setting for the interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostinterface/copypipe(withaddress:))*