# SystemDependency

**Framework**: RealityKit  
**Kind**: enum

Defines update order relative to other systems. An object that specifies the update order between multiple systems.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
enum SystemDependency
```

#### Overview

Add instances of `SystemDependency` to your system’s [`dependencies`](system/dependencies.md) array to indicate whether RealityKit updates another specified system before or after this system.

## Topics

### Update order
- [case before(any System.Type)](systemdependency/before(_:).md)
  An update order that requests RealityKit update this system before it updates another specified system.
- [case after(any System.Type)](systemdependency/after(_:).md)
  An update order that requests RealityKit update this system after it updates another specified system.
### Comparisons
- [static func == (SystemDependency, SystemDependency) -> Bool](systemdependency/==(_:_:).md)
  Returns a Boolean value that indicates whether two dependencies are equal.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static var dependencies: [SystemDependency]](system/dependencies.md)
  An array of dependencies for this system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/systemdependency)*