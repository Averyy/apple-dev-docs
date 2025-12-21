# BEAccessibilityRemoteHostElement

**Framework**: BrowserEngineKit  
**Kind**: class

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class BEAccessibilityRemoteHostElement
```

#### Overview

BEAccessibilityRemoteHostElement connects the accessibility hierarchy of two separate processes. The remote host and remote elements share the same identifier to facilitate this connection. To use this, return this remote element from an object in your view hierarchy via its `accessibilityElements` method.

## Topics

### Initializers
- [init(identifier: String, remotePid: pid_t)](beaccessibilityremotehostelement/init(identifier:remotepid:).md)
### Instance Properties
- [var accessibilityContainer: AnyObject?](beaccessibilityremotehostelement/accessibilitycontainer.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibilityremotehostelement)*