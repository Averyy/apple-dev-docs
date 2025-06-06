# matchDomains

**Framework**: Network Extension  
**Kind**: property

The hostname domains that match the rule.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var matchDomains: [Any]? { get set }
```

#### Discussion

If this property is set to a nonempty array, then only connections to destinations in the domains specified in the array will use the VPN.

## See Also

- [var matchSigningIdentifier: String](neapprule/matchsigningidentifier.md)
  The signing identifier of the app that matches the rule.
- [var matchDesignatedRequirement: String](neapprule/matchdesignatedrequirement.md)
  The designated requirement of the app that matches the rule.
- [var matchPath: String?](neapprule/matchpath.md)
  The file system path of the app that matches the rule.
- [var matchTools: [NEAppRule]?](neapprule/matchtools.md)
  An array of app rule objects that restrict the rule so it only matches network traffic generated from helper processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapprule/matchdomains)*