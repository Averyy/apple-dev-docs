# needRules()

**Framework**: Network Extension  
**Kind**: method  
**Role**: Type Method

Creates a verdict that tells the system that the Filter Control Provider needs to update the rules before making a decision about the flow’s data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func needRules() -> NEFilterDataVerdict
```

```objc
+ (NEFilterDataVerdict *) needRulesVerdict;
```

#### Return Value

A `NEFilterDataVerdict` object.

#### Discussion

When the Filter Data Provider returns this verdict, the system passes the flow to the Filter Control Provider’s [`handleNewFlow(_:completionHandler:)`](../nefiltercontrolprovider/handlenewflow%28_,completionhandler%29.md) method.

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
- [init(passBytes: Int, peekBytes: Int)](./init%28passbytes,peekbytes%29.md)
  Creates a verdict that tells the system to pass a chunk of network data to its final destination, and specifies the next chunk of data to provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterdataverdict/needrules())*