# matchPath

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The file system path of the app that matches the rule.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var matchPath: String? { get set }
```

```objc
@property (copy, nullable) NSString * matchPath;
```

## See Also

### Accessing app rule properties
- [var matchSigningIdentifier: String](./matchsigningidentifier.md)
  The signing identifier of the app that matches the rule.
- [var matchDesignatedRequirement: String](./matchdesignatedrequirement.md)
  The designated requirement of the app that matches the rule.
- [var matchDomains: [Any]?](./matchdomains.md)
  The hostname domains that match the rule.
- [var matchTools: [NEAppRule]?](./matchtools.md)
  An array of app rule objects that restrict the rule so it only matches network traffic generated from helper processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapprule/matchpath)*