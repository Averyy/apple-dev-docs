# handleRemediation(for:)

**Framework**: Network Extension  
**Kind**: method

Handle a remediation request.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func handleRemediation(for flow: NEFilterFlow) -> NEFilterRemediationVerdict
```

#### Return Value

An [`NEFilterRemediationVerdict`](nefilterremediationverdict.md) object indicating how the system should handle the flow of network content.

#### Discussion

The system calls this method when the user taps or clicks on the remediation link in the “block” web page in a WebKit browser object and the target of the remediation link is not set to a web page.

`NEFilterDataProvider` subclasses must override this method.

## Parameters

- `flow`: An   object containing information about the flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterdataprovider/handleremediation(for:))*