# init(signingIdentifier:)

**Framework**: Network Extension  
**Kind**: init  
**Role**: Initializer

Create an app rule that matches an app with a given signing identifier.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(signingIdentifier: String)
```

```objc
- (instancetype) initWithSigningIdentifier:(NSString *) signingIdentifier;
```

## Return Value

A newly-initialized `NEAppRule` object.

## Parameters

- `signingIdentifier`: The signing identifier of the app that matches the rule. For apps that are signed using Xcode, the app’s signing identifier is equivalent to the app’s bundle identifier.

## See Also

### Initializing an app rule
- [init(signingIdentifier: String, designatedRequirement: String)](./init%28signingidentifier,designatedrequirement%29.md)
  Create an app rule that matches an app with a given signing identifier and a given designated requirement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapprule/init(signingidentifier:))*