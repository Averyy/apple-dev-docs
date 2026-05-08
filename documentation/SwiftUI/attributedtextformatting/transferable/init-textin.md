# init(text:in:)

**Framework**: SwiftUI  
**Kind**: init

Create a transferable representation of an attributed string as interpreted in a SwiftUI environment.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(text: AttributedString, in environment: EnvironmentValues)
```

#### Discussion

When exporting the `text` into different data formats, the transfer representation may use the given `environment` to resolve semantic attribute values, such as certain colors or fonts to concrete values. This means that depending on the representation used during transfer, some semantic information may be lost in that step.

> **Note**: The transferable representation applies the [`AttributedTextFormattingDefinition`](attributedtextformattingdefinition.md) in the `environment` before exporting the content.

> **Note**: `View/attributedTextFormattingDefinition(_:)-uc57`, `AttributedTextValueConstraint/constrain(_:)-6cp64`


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextformatting/transferable/init(text:in:))*