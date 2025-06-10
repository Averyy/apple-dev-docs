# PreviewRegistry

**Framework**: DeveloperToolsSupport  
**Kind**: protocol

A protocol that the system uses to locate previews at runtime.

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
protocol PreviewRegistry
```

#### Overview

Preview macros make use of this protocol on your behalf. Don’t use it directly. Instead, use one of the preview macros, like [`Preview(_:body:)`](https://developer.apple.com/documentation/SwiftUI/Preview(_:body:)).

> ❗ **Important**: If you define a preview registry directly, the behavior is undefined.

## Topics

### Type Properties
- [static var column: Int](previewregistry/column.md)
- [static var fileID: String](previewregistry/fileid.md)
- [static var line: Int](previewregistry/line.md)
- [static var preview: Preview](previewregistry/preview.md)
### Type Methods
- [static func makePreview() throws -> Preview](previewregistry/makepreview.md)

## See Also

- [struct Preview](preview.md)
  A base type that preview macros use to create previews.
- [enum PreviewLayout](previewlayout.md)
  A size constraint for a preview.
- [struct PreviewTrait](previewtrait.md)
  Customizations that you can apply to a preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/previewregistry)*