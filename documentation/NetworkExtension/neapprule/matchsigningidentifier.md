# matchSigningIdentifier

**Framework**: Network Extension  
**Kind**: property

The signing identifier of the app that matches the rule.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var matchSigningIdentifier: String { get }
```

## See Also

- [var matchDesignatedRequirement: String](neapprule/matchdesignatedrequirement.md)
  The designated requirement of the app that matches the rule.
- [var matchPath: String?](neapprule/matchpath.md)
  The file system path of the app that matches the rule.
- [var matchDomains: [Any]?](neapprule/matchdomains.md)
  The hostname domains that match the rule.
- [var matchTools: [NEAppRule]?](neapprule/matchtools.md)
  An array of app rule objects that restrict the rule so it only matches network traffic generated from helper processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapprule/matchsigningidentifier)*