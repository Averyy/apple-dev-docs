# enabled

**Framework**: AppKit  
**Kind**: property

Spring-loading on the destination object is enabled. The user can drag an object over a destination object and hover or force click to initiate spring-loading and activate the destination object. When initiated by a force click, spring-loading is invoked once the force click is released.

**Availability**:
- macOS 10.11+

## Declaration

```swift
static var enabled: NSSpringLoadingOptions { get }
```

## See Also

- [static var disabled: NSSpringLoadingOptions](nsspringloadingoptions/disabled.md)
  Spring-loading on the destination object is disabled. No spring-loading operations can occur.
- [static var continuousActivation: NSSpringLoadingOptions](nsspringloadingoptions/continuousactivation.md)
  Spring-loading on the destination object is enabled. The user can drag an object over a destination object and hover or force click to initiate spring-loading and activate the destination object. When initiated by a force click, spring-loading is invoked once the force click begins and deactivated when the force click is released. When initiated by hovering, spring-loading is invoked at the hover timeout and deactivated when the drag exits the destination object. Use this constant sparingly.
- [static var noHover: NSSpringLoadingOptions](nsspringloadingoptions/nohover.md)
  Spring-loading on the destination object is enabled, but cannot be invoked by hovering. The user can drag an object over a destination object and force click to initiate spring-loading and activate the destination object. This option may be useful in situations where a long hover, such as dragging across a large destination object, initiates undesired spring-loading. Use this constant sparingly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspringloadingoptions/enabled)*