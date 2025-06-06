# NSSpringLoadingOptions

**Framework**: AppKit  
**Kind**: struct

These constants denote the type of spring-loading behavior configured for the destination object.

**Availability**:
- macOS 10.11+

## Declaration

```swift
struct NSSpringLoadingOptions
```

## Topics

### Constants
- [static var disabled: NSSpringLoadingOptions](nsspringloadingoptions/disabled.md)
  Spring-loading on the destination object is disabled. No spring-loading operations can occur.
- [static var enabled: NSSpringLoadingOptions](nsspringloadingoptions/enabled.md)
  Spring-loading on the destination object is enabled. The user can drag an object over a destination object and hover or force click to initiate spring-loading and activate the destination object. When initiated by a force click, spring-loading is invoked once the force click is released.
- [static var continuousActivation: NSSpringLoadingOptions](nsspringloadingoptions/continuousactivation.md)
  Spring-loading on the destination object is enabled. The user can drag an object over a destination object and hover or force click to initiate spring-loading and activate the destination object. When initiated by a force click, spring-loading is invoked once the force click begins and deactivated when the force click is released. When initiated by hovering, spring-loading is invoked at the hover timeout and deactivated when the drag exits the destination object. Use this constant sparingly.
- [static var noHover: NSSpringLoadingOptions](nsspringloadingoptions/nohover.md)
  Spring-loading on the destination object is enabled, but cannot be invoked by hovering. The user can drag an object over a destination object and force click to initiate spring-loading and activate the destination object. This option may be useful in situations where a long hover, such as dragging across a large destination object, initiates undesired spring-loading. Use this constant sparingly.
### Initializers
- [init(rawValue: UInt)](nsspringloadingoptions/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspringloadingoptions)*