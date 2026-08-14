# CVAttachmentModePreference

**Framework**: Core Video  
**Kind**: protocol

Defines preferred mode for an attachment key.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
protocol CVAttachmentModePreference : Sendable
```

#### Overview

This protocol is used to identify the mode preferences in generic context. You should use one of the [`CVAttachmentModePreferenceShouldPropagate`](cvattachmentmodepreferenceshouldpropagate.md) or [`CVAttachmentModePreferenceShouldNotPropagate`](cvattachmentmodepreferenceshouldnotpropagate.md) instead of defining a custom conformance to this protocol.

## Topics

### Type Properties
- [static var preferredMode: CVAttachmentMode](cvattachmentmodepreference/preferredmode.md)

## Relationships

### Inherits From
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
### Conforming Types
- [CVAttachmentModePreferenceShouldNotPropagate](cvattachmentmodepreferenceshouldnotpropagate.md)
- [CVAttachmentModePreferenceShouldPropagate](cvattachmentmodepreferenceshouldpropagate.md)

## See Also

- [protocol CVBufferRepresentable](cvbufferrepresentable.md)
  CVBufferRepresentable protocol is a sealed protocol intended to be implemented by the types in CoreVideo framework. This protocol facilitates Swift types that wrap a value of CVBuffer type.
- [protocol CVAttachmentKeyDefinitions](cvattachmentkeydefinitions.md)
  Marks a type as a collection of attachment keys for an attachment bearer.
- [protocol CVAttachmentValueRepresentable](cvattachmentvaluerepresentable.md)
  Allows Swift types to be used as buffer attachment value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvattachmentmodepreference)*