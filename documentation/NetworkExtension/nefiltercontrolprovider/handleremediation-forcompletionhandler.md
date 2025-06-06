# handleRemediation(for:completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Handle a request for remediation from the user.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func handleRemediation(for flow: NEFilterFlow) async -> NEFilterControlVerdict
```

#### Discussion

This method is called by the system when the Filter Data Provider indicates that the filtering verdict for the given flow is `NEFilterRemediateVerdictNeedRules`. Subclass implementations must override this method and implement whatever steps are necessary to remediate the given flow.

## Parameters

- `flow`: An   object containing details about the flow that requires remediation.
- `completionHandler`: A block that must be called when the Filter Control Provider has made a decision about the flow. The   object passed to this block contains the decision that the Filter Control Provider made about the flow.

## See Also

- [var remediationMap: [String : [String : NSObject]]?](nefiltercontrolprovider/remediationmap.md)
  A dictionary containing sets of strings used to customize the remediation portion of the block page.
- [let NEFilterProviderRemediationMapRemediationButtonTexts: String](nefilterproviderremediationmapremediationbuttontexts.md)
  A key in the [`remediationMap`](nefiltercontrolprovider/remediationmap.md) dictionary. The value of this key should be set to a dictionary that maps button text string identifiers to the text to display for the remediation URL link in the block page. The button text string identifiers are defined by the Filter Control Provider app extension.
- [let NEFilterProviderRemediationMapRemediationURLs: String](nefilterproviderremediationmapremediationurls.md)
  A key in the [`remediationMap`](nefiltercontrolprovider/remediationmap.md) dictionary. The value of this key should be set to a dictionary that maps URL identifiers to remediation URLs to be inserted into the block page. The URL identifiers are defined by the Filter Control Provider app extension.
- [var NEFilterProviderRemediationURLFlowURL: String](nefilterproviderremediationurlflowurl.md)
  This string will be replaced with the full URL of the flow.
- [var NEFilterProviderRemediationURLFlowURLHostname: String](nefilterproviderremediationurlflowurlhostname.md)
  This string will be replaced with the hostname portion of the flow’s URL.
- [var NEFilterProviderRemediationURLOrganization: String](nefilterproviderremediationurlorganization.md)
  This string will be replaced with the value of the organization property set in the filter configuration.
- [var NEFilterProviderRemediationURLUsername: String](nefilterproviderremediationurlusername.md)
  This string will be replaced with the value of the username property set in the filter configuration.
- [var urlAppendStringMap: [String : String]?](nefiltercontrolprovider/urlappendstringmap.md)
  A dictionary containing strings to be appended to URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltercontrolprovider/handleremediation(for:completionhandler:))*