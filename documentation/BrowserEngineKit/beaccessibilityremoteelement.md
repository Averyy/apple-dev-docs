# BEAccessibilityRemoteElement

**Framework**: BrowserEngineKit  
**Kind**: class

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class BEAccessibilityRemoteElement
```

#### Overview

BEAccessibilityRemoteElement represents the destination of a BEAccessibilityRemoteHostElement in a different process. The elements it contains are defined by the `accessibilityElements` API. `BEAccessibilityRemoteElement` does not need to be returned in any element array.

## Topics

### Initializers
- [init(identifier: String, hostPid: pid_t)](beaccessibilityremoteelement/init(identifier:hostpid:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beaccessibilityremoteelement)*