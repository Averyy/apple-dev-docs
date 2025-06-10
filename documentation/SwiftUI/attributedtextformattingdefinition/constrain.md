# constrain(_:)

**Framework**: SwiftUI  
**Kind**: method

Applies all value constraints to a given attribute container.

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
func constrain(_ container: inout AttributeContainer)
```

#### Discussion

Modifies the given `container` by applying all [`AttributedTextValueConstraint`](attributedtextvalueconstraint.md)s that are part of this definition to the container.

Use this function to test your [`AttributedTextFormattingDefinition`](attributedtextformattingdefinition.md), or to ensure your constraints are applied before passing content to API that cannot itself apply the definition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextformattingdefinition/constrain(_:))*