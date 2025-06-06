# allow()

**Framework**: Network Extension  
**Kind**: method

Creates a verdict that tells the system to pass the current chunk of network data and all subsequent data for the current flow to its final destination.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class func allow() -> NEFilterDataVerdict
```

#### Return Value

A `NEFilterDataVerdict` object.

## See Also

- [class func drop() -> NEFilterDataVerdict](nefilterdataverdict/drop.md)
  Creates a verdict that tells the system to drop the current chunk of network data and all subsequent data for the current flow.
- [class func pause() -> NEFilterDataVerdict](nefilterdataverdict/pause.md)
  Creates a verdict that tells the system to pause the flow.
- [class func remediateVerdict(withRemediationURLMapKey: String?, remediationButtonTextMapKey: String?) -> NEFilterDataVerdict](nefilterdataverdict/remediateverdict(withremediationurlmapkey:remediationbuttontextmapkey:).md)
  Creates a verdict to drop the current chunk of network data and all subsequent data for the current flow, and provides a remediation URL.
- [class func needRules() -> NEFilterDataVerdict](nefilterdataverdict/needrules.md)
  Creates a verdict that tells the system that the Filter Control Provider needs to update the rules before making a decision about the flow’s data.
- [init(passBytes: Int, peekBytes: Int)](nefilterdataverdict/init(passbytes:peekbytes:).md)
  Creates a verdict that tells the system to pass a chunk of network data to its final destination, and specifies the next chunk of data to provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterdataverdict/allow())*