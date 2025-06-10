# init(transferable:in:)

**Framework**: Foundation  
**Kind**: init

Extract an attributed string from SwiftUI’s transferable representation in a certain environment.

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
init(transferable: AttributedTextFormatting.Transferable, in environment: EnvironmentValues) throws
```

#### Discussion

Use this initializer with a `AttributedTextFormatting/Transferable` that was imported, e.g. in the `action` closure of the `View/dropDestination(for:action:isTargeted)` modifier.

> **Note**: This initializer applies the `AttributedTextFormattingDefinition` in the given `environment` to the imported text before returning.

> **Note**: `View/attributedTextFormattingDefinition(_:)-uc57`, `AttributedTextValueConstraint/constrain(_:)-6cp64`


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/init(transferable:in:))*