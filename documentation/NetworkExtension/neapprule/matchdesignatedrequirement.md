# matchDesignatedRequirement

**Framework**: Network Extension  
**Kind**: property

The designated requirement of the app that matches the rule.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var matchDesignatedRequirement: String { get }
```

## See Also

- [var matchSigningIdentifier: String](neapprule/matchsigningidentifier.md)
  The signing identifier of the app that matches the rule.
- [var matchPath: String?](neapprule/matchpath.md)
  The file system path of the app that matches the rule.
- [var matchDomains: [Any]?](neapprule/matchdomains.md)
  The hostname domains that match the rule.
- [var matchTools: [NEAppRule]?](neapprule/matchtools.md)
  An array of app rule objects that restrict the rule so it only matches network traffic generated from helper processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapprule/matchdesignatedrequirement)*