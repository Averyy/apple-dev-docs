# SystemDependency

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

Defines update order relative to other systems. An object that specifies the update order between multiple systems.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
enum SystemDependency
```

## Overview

Add instances of `SystemDependency` to your system’s [`dependencies`](./system/dependencies.md) array to indicate whether RealityKit updates another specified system before or after this system.

## Topics

### Update order
- [case before(any System.Type)](./systemdependency/before%28_%29.md)
  An update order that requests RealityKit update this system before it updates another specified system.
- [case after(any System.Type)](./systemdependency/after%28_%29.md)
  An update order that requests RealityKit update this system after it updates another specified system.
### Operators
- [static func == (SystemDependency, SystemDependency) -> Bool](./systemdependency/eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two dependencies are equal.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Specifying dependencies
- [static var dependencies: [SystemDependency]](./system/dependencies.md)
  An array of dependencies for this system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/systemdependency)*