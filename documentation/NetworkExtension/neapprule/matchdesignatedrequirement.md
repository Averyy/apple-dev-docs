# matchDesignatedRequirement

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The designated requirement of the app that matches the rule.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var matchDesignatedRequirement: String { get }
```

```objc
@property (readonly) NSString * matchDesignatedRequirement;
```

## See Also

### Accessing app rule properties
- [var matchSigningIdentifier: String](./matchsigningidentifier.md)
  The signing identifier of the app that matches the rule.
- [var matchPath: String?](./matchpath.md)
  The file system path of the app that matches the rule.
- [var matchDomains: [Any]?](./matchdomains.md)
  The hostname domains that match the rule.
- [var matchTools: [NEAppRule]?](./matchtools.md)
  An array of app rule objects that restrict the rule so it only matches network traffic generated from helper processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapprule/matchdesignatedrequirement)*