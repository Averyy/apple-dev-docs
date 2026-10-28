# portCoderWithReceivePort:sendPort:components:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns a new `NSPortCoder` object.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```objc
+ (id) portCoderWithReceivePort:(NSPort *) rcvPort sendPort:(NSPort *) sndPort components:(NSArray *) comps;
```

## Return Value

A new `NSPortCoder` object connected to the communication ports `rcvPort` and `sndPort`, with an encoded distributed objects message stored in `comps`.

## Parameters

- `rcvPort`: The receiver port.
- `sndPort`: The send port.
- `comps`: An array containing an encoded distributed objects message.

## See Also

### Related Documentation
- [- dispatch](./dispatch.md)
  Processes and acts upon the distributed object message with which the receiver was initialized.
- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)
### Creating an NSPortCoder Object
- [- initWithReceivePort:sendPort:components:](./initwithreceiveport_sendport_components_.md)
  Initializes and returns an `NSPortCoder` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsportcoder/portcoderwithreceiveport:sendport:components:)*