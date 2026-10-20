# init(text:in:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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

> **Note**: The transferable representation applies the [`AttributedTextFormattingDefinition`](../../attributedtextformattingdefinition.md) in the `environment` before exporting the content.

> **See Also**: [`attributedTextFormattingDefinition(_:)`](../../view/attributedtextformattingdefinition%28_%29-81jn6.md), `AttributedTextValueConstraint/constrain(_:)-6cp64`


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextformatting/transferable/init(text:in:))*