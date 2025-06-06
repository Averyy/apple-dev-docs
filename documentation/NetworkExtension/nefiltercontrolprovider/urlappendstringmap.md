# urlAppendStringMap

**Framework**: Network Extension  
**Kind**: property

A dictionary containing strings to be appended to URLs.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var urlAppendStringMap: [String : String]? { get set }
```

#### Discussion

When the Filter Data Provider determines that a string should be appended to the request URL for a new flow, it creates a [`NEFilterNewFlowVerdict`](nefilternewflowverdict.md) object using the `URLAppendStringVerdictWithMapKey:` class method. The system uses the `URLAppendStringVerdictWithMapKey:` method to look up the corresponding string in this dictionary. The system then appends the string to the flow’s request URL.

## See Also

- [func handleRemediation(for: NEFilterFlow, completionHandler: (NEFilterControlVerdict) -> Void)](nefiltercontrolprovider/handleremediation(for:completionhandler:).md)
  Handle a request for remediation from the user.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltercontrolprovider/urlappendstringmap)*