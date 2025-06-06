# remediateVerdict(withRemediationURLMapKey:remediationButtonTextMapKey:)

**Framework**: Network Extension  
**Kind**: method

Creates a verdict to drop the current chunk of network data and all subsequent data for the current flow, and provides a remediation URL.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func remediateVerdict(withRemediationURLMapKey remediationURLMapKey: String?, remediationButtonTextMapKey: String?) -> NEFilterDataVerdict
```

#### Return Value

A `NEFilterDataVerdict` object.

#### Discussion

When the Filter Data Provider returns this verdict from one of its data filtering methods, the system resolves the verdict as follows:

1. The system uses the verdict’s `remediationURLMapKey` and `remediationButtonTextMapKey` to look up the remediation URL parameters in the [`remediationMap`](nefiltercontrolprovider/remediationmap.md) dictionary set by the Filter Control Provider.
2. The system then inserts the remediation URL parameters into the block page and presents it to the user.

The user can tap the URL to appeal the decision to drop the flow. This starts the remediation process, if your app provides one.

## Parameters

- `remediationURLMapKey`: The key in the Filter Control Provider’s   dictionary corresponding to the URL of the remediation link to give to the user.
- `remediationButtonTextMapKey`: The key in the Filter Control Provider’s   dictionary that corresponds to the text of the remediation link text to give to the user.

## See Also

- [class func allow() -> NEFilterDataVerdict](nefilterdataverdict/allow.md)
  Creates a verdict that tells the system to pass the current chunk of network data and all subsequent data for the current flow to its final destination.
- [class func drop() -> NEFilterDataVerdict](nefilterdataverdict/drop.md)
  Creates a verdict that tells the system to drop the current chunk of network data and all subsequent data for the current flow.
- [class func pause() -> NEFilterDataVerdict](nefilterdataverdict/pause.md)
  Creates a verdict that tells the system to pause the flow.
- [class func needRules() -> NEFilterDataVerdict](nefilterdataverdict/needrules.md)
  Creates a verdict that tells the system that the Filter Control Provider needs to update the rules before making a decision about the flow’s data.
- [init(passBytes: Int, peekBytes: Int)](nefilterdataverdict/init(passbytes:peekbytes:).md)
  Creates a verdict that tells the system to pass a chunk of network data to its final destination, and specifies the next chunk of data to provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterdataverdict/remediateverdict(withremediationurlmapkey:remediationbuttontextmapkey:))*