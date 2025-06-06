# pause()

**Framework**: Network Extension  
**Kind**: method

Creates a verdict that tells the system to pause the flow.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class func pause() -> NEFilterDataVerdict
```

#### Return Value

A `NEFilterDataVerdict` object.

#### Discussion

After pausing the flow, the system doesn’t call any of the data provider’s handler callbacks until you resume the flow by calling [`resumeFlow(_:with:)`](nefilterdataprovider/resumeflow(_:with:).md).

You can pause TCP flows indefinitely. You can pause UDP flows for up to 10 seconds, after which the system drops the flow. Pausing a flow that’s already paused is an invalid operation.

## See Also

- [class func allow() -> NEFilterDataVerdict](nefilterdataverdict/allow.md)
  Creates a verdict that tells the system to pass the current chunk of network data and all subsequent data for the current flow to its final destination.
- [class func drop() -> NEFilterDataVerdict](nefilterdataverdict/drop.md)
  Creates a verdict that tells the system to drop the current chunk of network data and all subsequent data for the current flow.
- [class func remediateVerdict(withRemediationURLMapKey: String?, remediationButtonTextMapKey: String?) -> NEFilterDataVerdict](nefilterdataverdict/remediateverdict(withremediationurlmapkey:remediationbuttontextmapkey:).md)
  Creates a verdict to drop the current chunk of network data and all subsequent data for the current flow, and provides a remediation URL.
- [class func needRules() -> NEFilterDataVerdict](nefilterdataverdict/needrules.md)
  Creates a verdict that tells the system that the Filter Control Provider needs to update the rules before making a decision about the flow’s data.
- [init(passBytes: Int, peekBytes: Int)](nefilterdataverdict/init(passbytes:peekbytes:).md)
  Creates a verdict that tells the system to pass a chunk of network data to its final destination, and specifies the next chunk of data to provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterdataverdict/pause())*