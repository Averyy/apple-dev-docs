# AVMediaPresentationSelector

**Framework**: AVFoundation  
**Kind**: class

For content that has been authored with the express intent of offering an alternative selection interface for AVMediaSelectionOptions, AVMediaPresentationSelector represents a collection of mutually exclusive settings.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
class AVMediaPresentationSelector
```

#### Overview

Subclasses of this type that are used from Swift must fulfill the requirements of a Sendable type.

## Topics

### Instance Properties
- [var identifier: String](avmediapresentationselector/identifier.md)
  Provides the authored identifier for the selector.
- [var settings: [AVMediaPresentationSetting]](avmediapresentationselector/settings.md)
  Provides selectable mutually exclusive settings for the selector.
### Instance Methods
- [func displayName(forLocaleIdentifier: String) -> String](avmediapresentationselector/displayname(forlocaleidentifier:).md)
  Returns the display name for the selector that best matches the specified locale identifier.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediapresentationselector)*