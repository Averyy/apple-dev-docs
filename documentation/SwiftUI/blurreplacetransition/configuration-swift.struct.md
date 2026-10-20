# BlurReplaceTransition.Configuration

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

Configuration properties for a transition.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct Configuration
```

## Topics

### Getting the transition configuration
- [static let downUp: BlurReplaceTransition.Configuration](./configuration-swift.struct/downup.md)
  A configuration that requests a transition that scales the view down while removing it and up while inserting it.
- [static let upUp: BlurReplaceTransition.Configuration](./configuration-swift.struct/upup.md)
  A configuration that requests a transition that scales the view up while both removing and inserting it.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating the transition
- [init(configuration: BlurReplaceTransition.Configuration)](./init%28configuration%29.md)
  Creates a new transition.
- [var configuration: BlurReplaceTransition.Configuration](./configuration-swift.property.md)
  The transition configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/blurreplacetransition/configuration-swift.struct)*