# matchSigningIdentifier

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) NSString * matchSigningIdentifier;
```

## See Also

### Accessing app rule properties
- [var matchDesignatedRequirement: String](./matchdesignatedrequirement.md)
  The designated requirement of the app that matches the rule.
- [var matchPath: String?](./matchpath.md)
  The file system path of the app that matches the rule.
- [var matchDomains: [Any]?](./matchdomains.md)
  The hostname domains that match the rule.
- [var matchTools: [NEAppRule]?](./matchtools.md)
  An array of app rule objects that restrict the rule so it only matches network traffic generated from helper processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapprule/matchsigningidentifier)*