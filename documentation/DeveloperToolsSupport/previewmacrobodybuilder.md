# PreviewMacroBodyBuilder

**Framework**: DeveloperToolsSupport  
**Kind**: struct

Builder for preview body content within a `#Preview` macro.

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
@resultBuilder
struct PreviewMacroBodyBuilder<Content>
```

#### Overview

> ⚠️ **Warning**: Using this builder outside of a `#Preview` macro will produce a fatal error.

Using this builder outside of a `#Preview` macro will produce a fatal error.

## Topics

### Type Methods
- [static func buildBlock(Content) -> Content](previewmacrobodybuilder/buildblock(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/previewmacrobodybuilder)*