# continuousActivation

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Spring-loading on the destination object is enabled. The user can drag an object over a destination object and hover or force click to initiate spring-loading and activate the destination object. When initiated by a force click, spring-loading is invoked once the force click begins and deactivated when the force click is released. When initiated by hovering, spring-loading is invoked at the hover timeout and deactivated when the drag exits the destination object. Use this constant sparingly.

**Availability**:
- macOS 10.11+

## Declaration

```swift
static var continuousActivation: NSSpringLoadingOptions { get }
```

```c
NSSpringLoadingContinuousActivation
```

## See Also

### Constants
- [static var disabled: NSSpringLoadingOptions](./disabled.md)
  Spring-loading on the destination object is disabled. No spring-loading operations can occur.
- [static var enabled: NSSpringLoadingOptions](./enabled.md)
  Spring-loading on the destination object is enabled. The user can drag an object over a destination object and hover or force click to initiate spring-loading and activate the destination object. When initiated by a force click, spring-loading is invoked once the force click is released.
- [static var noHover: NSSpringLoadingOptions](./nohover.md)
  Spring-loading on the destination object is enabled, but cannot be invoked by hovering. The user can drag an object over a destination object and force click to initiate spring-loading and activate the destination object. This option may be useful in situations where a long hover, such as dragging across a large destination object, initiates undesired spring-loading. Use this constant sparingly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspringloadingoptions/continuousactivation)*