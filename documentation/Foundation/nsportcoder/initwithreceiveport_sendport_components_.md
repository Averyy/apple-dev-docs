# initWithReceivePort:sendPort:components:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Initializes and returns an `NSPortCoder` object.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```objc
- (id) initWithReceivePort:(NSPort *) rcvPort sendPort:(NSPort *) sndPort components:(NSArray *) comps;
```

## Discussion

Initializes a newly allocated `NSPortCoder` object connected to the communication ports `rcvPort` and `sndPort`, with an encoded distributed objects message stored in `comps`.

## Parameters

- `rcvPort`: The receive port.
- `sndPort`: The send port.
- `comps`: An array containing an encoded distributed objects message.

## See Also

### Related Documentation
- [- dispatch](./dispatch.md)
  Processes and acts upon the distributed object message with which the receiver was initialized.
### Creating an NSPortCoder Object
- [+ portCoderWithReceivePort:sendPort:components:](./portcoderwithreceiveport_sendport_components_.md)
  Creates and returns a new `NSPortCoder` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsportcoder/initwithreceiveport:sendport:components:)*