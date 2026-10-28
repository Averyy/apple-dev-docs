# Text.Scale

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

Defines text scales

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
struct Scale
```

## Overview

Text scale provides a way to pick a logical text scale relative to the base font which is used.

## Topics

### Getting built-in text scales
- [static let `default`: Text.Scale](./scale/default.md)
  Defines default text scale
- [static let secondary: Text.Scale](./scale/secondary.md)
  Defines secondary text scale

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Fitting text into available space
- [func textScale(Text.Scale, isEnabled: Bool) -> Text](./textscale%28_,isenabled%29.md)
  Applies a text scale to the text.
- [Text.TruncationMode](./truncationmode.md)
  The type of truncation to apply to a line of text when it’s too long to fit in the available space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/scale)*