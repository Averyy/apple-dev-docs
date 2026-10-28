# constrain(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Applies all value constraints to a given attributed string.

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
func constrain(_ string: inout AttributedString)
```

**Other overloads**:

```swift
func constrain(_ container: inout AttributeContainer)
```

## Discussion

Modifies the given `string` by applying all [`AttributedTextValueConstraint`](../attributedtextvalueconstraint.md)s that are part of this definition to each run of the string.

Use this function to test your [`AttributedTextFormattingDefinition`](../attributedtextformattingdefinition.md), or to ensure your constraints are applied before passing content to API that cannot itself apply the definition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextformattingdefinition/constrain(_:)-1ur9c)*