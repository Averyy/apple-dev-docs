# init(signingIdentifier:)

**Framework**: Network Extension  
**Kind**: init

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

#### Return Value

A newly-initialized `NEAppRule` object.

## Parameters

- `signingIdentifier`: The signing identifier of the app that matches the rule. For apps that are signed using Xcode, the app’s signing identifier is equivalent to the app’s bundle identifier.

## See Also

- [init(signingIdentifier: String, designatedRequirement: String)](neapprule/init(signingidentifier:designatedrequirement:).md)
  Create an app rule that matches an app with a given signing identifier and a given designated requirement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapprule/init(signingidentifier:))*