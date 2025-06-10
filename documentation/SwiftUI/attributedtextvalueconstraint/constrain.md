# constrain(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Enforce constraints on the attribute.

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
func constrain(_ container: inout Self.Attributes)
```

#### Discussion

A function that transforms the [`AttributeKey`](attributedtextvalueconstraint/attributekey.md) on the given `container` so it represents a formatting that the conforming type defines to be valid.

This function can generally read any attribute on `container` and it will produce a value that has been constrained by all [`AttributedTextValueConstraint`](attributedtextvalueconstraint.md) listed in the associated text formatting definition above the constraint reading the attribute.

Consider the following example:

```swift
struct NoEqualForegroundAndBackground: AttributedTextValueConstraint {
    typealias Scope = MyTextFormattingDefinition.Scope
    typealias AttributeKey = AttributeScopes.SwiftUIAttributes.BackgroundColorAttribute

    func constrain(
        _ container: inout Attributes
    ) {
        if let color = container.foregroundColor,
           container.backgroundColor == color
        {
            container.backgroundColor = nil
        }
    }
}
```

When this constrain function accesses `container.foregroundColor`, the system establishes that the background color depends on the foreground color. At that time, it checks if the [`AttributedTextFormattingDefinition`](attributedtextformattingdefinition.md) this constraint is part of defines constraints on the foreground color  `NoEqualForegroundAndBackground` and applies them. Thus, when the access to `container.foregroundColor` returns, this function reads the constrained value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextvalueconstraint/constrain(_:))*