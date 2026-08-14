# PresentationPlacement

**Framework**: SwiftUI  
**Kind**: struct

The placement of a presentation within the presenting view.

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
struct PresentationPlacement
```

#### Overview

Only sheet presentations respect this placement.

Use values of this type with the [`presentationPlacement(_:)`](view/presentationplacement(_:).md) modifier.

## Topics

### Type Properties
- [static let automatic: PresentationPlacement](presentationplacement/automatic.md)
  The system determines the placement of the presentation.
- [static let center: PresentationPlacement](presentationplacement/center.md)
  Centers the presentation within the presenting view.
- [static let leading: PresentationPlacement](presentationplacement/leading.md)
  Places the presentation on the leading edge of the presenting view.
- [static let trailing: PresentationPlacement](presentationplacement/trailing.md)
  Places the presentation on the trailing edge of the presenting view.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/presentationplacement)*