# attributedTextFormattingDefinition(_:)

**Framework**: FamilyControls  
**Kind**: method

Apply an attribute-only text formatting definition to all nested editor views.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func attributedTextFormattingDefinition<S>(_ scope: S.Type) -> some View where S : AttributeScope
```

#### Discussion

Using only an attribute scope for the text formatting definition allows the editor to use all attributes in the scope, but does not constrain their values in any way. To constrain what values attribute can have, use `attributedTextFormattingDefinition(_:)-81jn6`.

This example editor allows using Genmoji, but otherwise is a plain text editor:

```swift
struct MyAttributeScope: AttributeScope {
    let adaptiveImageGlyph: AttributeScopes.SwiftUIAttributes.AdaptiveImageGlyphAttribute
}

TextEditor(text: $text)
    .attributedTextFormattingDefinition(MyAttributeScope.self)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/attributedtextformattingdefinition(_:)-33x2g)*