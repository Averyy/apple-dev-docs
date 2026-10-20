# init(signingIdentifier:designatedRequirement:)

**Framework**: Network Extension  
**Kind**: init  
**Role**: Initializer

Create an app rule that matches an app with a given signing identifier and a given designated requirement.

**Availability**:
- macOS 10.11+

## Declaration

```swift
init(signingIdentifier: String, designatedRequirement: String)
```

```objc
- (instancetype) initWithSigningIdentifier:(NSString *) signingIdentifier designatedRequirement:(NSString *) designatedRequirement;
```

#### Return Value

A newly-initialized `NEAppRule` object.

## Parameters

- `signingIdentifier`: The signing identifier of the app that matches the rule. For apps that are signed using Xcode, the app’s signing identifier is equivalent to the app’s bundle identifier.
- `designatedRequirement`: The designated requirement of the app that matches the rule. The designated requirement for an app can be obtained using the `codesign` command-line developer tool.

## See Also

### Initializing an app rule
- [init(signingIdentifier: String)](./init%28signingidentifier%29.md)
  Create an app rule that matches an app with a given signing identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapprule/init(signingidentifier:designatedrequirement:))*