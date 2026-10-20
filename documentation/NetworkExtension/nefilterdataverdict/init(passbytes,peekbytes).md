# init(passBytes:peekBytes:)

**Framework**: Network Extension  
**Kind**: init  
**Role**: Initializer

Creates a verdict that tells the system to pass a chunk of network data to its final destination, and specifies the next chunk of data to provide.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
init(passBytes: Int, peekBytes: Int)
```

```objc
+ (NEFilterDataVerdict *) dataVerdictWithPassBytes:(NSUInteger) passBytes peekBytes:(NSUInteger) peekBytes;
```

#### Return Value

A `NEFilterDataVerdict` object.

## Parameters

- `passBytes`: The number of bytes to pass to its final destination.
- `peekBytes`: The number of bytes after the end of the `passBytes` that the Filter Data Provider expects in the next call to [`handleOutboundData(from:readBytesStartOffset:readBytes:)`](../nefilterdataprovider/handleoutbounddata%28from,readbytesstartoffset,readbytes%29.md) or [`handleInboundData(from:readBytesStartOffset:readBytes:)`](../nefilterdataprovider/handleinbounddata%28from,readbytesstartoffset,readbytes%29.md). The Filter Data Provider uses this chunk of data to make its next filtering decision.

  To see all subsequent bytes, set this parameter to [`NEFilterFlowBytesMax`](../nefilterflowbytesmax.md).

## See Also

### Creating data verdicts
- [class func allow() -> NEFilterDataVerdict](./allow%28%29.md)
  Creates a verdict that tells the system to pass the current chunk of network data and all subsequent data for the current flow to its final destination.
- [class func drop() -> NEFilterDataVerdict](./drop%28%29.md)
  Creates a verdict that tells the system to drop the current chunk of network data and all subsequent data for the current flow.
- [class func pause() -> NEFilterDataVerdict](./pause%28%29.md)
  Creates a verdict that tells the system to pause the flow.
- [class func remediateVerdict(withRemediationURLMapKey: String?, remediationButtonTextMapKey: String?) -> NEFilterDataVerdict](./remediateverdict%28withremediationurlmapkey,remediationbuttontextmapkey%29.md)
  Creates a verdict to drop the current chunk of network data and all subsequent data for the current flow, and provides a remediation URL.
- [class func needRules() -> NEFilterDataVerdict](./needrules%28%29.md)
  Creates a verdict that tells the system that the Filter Control Provider needs to update the rules before making a decision about the flow’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterdataverdict/init(passbytes:peekbytes:))*