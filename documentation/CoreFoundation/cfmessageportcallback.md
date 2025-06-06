# CFMessagePortCallBack

**Framework**: Core Foundation  
**Kind**: typealias

Callback invoked to process a message received on a CFMessagePort object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias CFMessagePortCallBack = (CFMessagePort?, Int32, CFData?, UnsafeMutableRawPointer?) -> Unmanaged<CFData>?
```

#### Return Value

Data to send back to the sender of the message. The system releases the returned CFData object. Return `NULL` if you want an empty reply returned to the sender.

#### Discussion

If you want the message data to persist beyond this callback, you must explicitly create a copy of `data` rather than merely retain it; the contents of `data` will be deallocated after the callback exits.

## Parameters

- `local`: The local message port that received the message.
- `msgid`: An arbitrary integer value assigned to the message by the sender.
- `data`: The message data.
- `info`: The   member of the   structure that was used when creating  .

## See Also

- [typealias CFMessagePortInvalidationCallBack](cfmessageportinvalidationcallback.md)
  Callback invoked when a CFMessagePort object is invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmessageportcallback)*