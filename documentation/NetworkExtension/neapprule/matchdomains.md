# matchDomains

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, nullable) NSArray * matchDomains;
```

## Discussion

If this property is set to a nonempty array, then only connections to destinations in the domains specified in the array will use the VPN.

## See Also

### Accessing app rule properties
- [var matchSigningIdentifier: String](./matchsigningidentifier.md)
  The signing identifier of the app that matches the rule.
- [var matchDesignatedRequirement: String](./matchdesignatedrequirement.md)
  The designated requirement of the app that matches the rule.
- [var matchPath: String?](./matchpath.md)
  The file system path of the app that matches the rule.
- [var matchTools: [NEAppRule]?](./matchtools.md)
  An array of app rule objects that restrict the rule so it only matches network traffic generated from helper processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapprule/matchdomains)*