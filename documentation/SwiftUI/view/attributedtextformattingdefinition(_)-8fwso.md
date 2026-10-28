# attributedTextFormattingDefinition(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Apply an attribute-only text formatting definition to all nested editor views.

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
nonisolated
func attributedTextFormattingDefinition<S>(_ scope: S.Type) -> some View where S : AttributeScope
```

**Other overloads**:

```swift
nonisolated
func attributedTextFormattingDefinition<D>(_ definition: D) -> some View where D : AttributedTextFormattingDefinition
```

```swift
nonisolated
func attributedTextFormattingDefinition<S>(_ path: KeyPath<AttributeScopes, S.Type>) -> some View where S : AttributeScope
```

## Discussion

Using only an attribute scope for the text formatting definition allows the editor to use all attributes in the scope, but does not constrain their values in any way. To constrain what values attribute can have, use [`attributedTextFormattingDefinition(_:)`](./attributedtextformattingdefinition%28_%29-81jn6.md).

This example editor allows using Genmoji, but otherwise is a plain text editor:

```swift
struct MyAttributeScope: AttributeScope {
    let adaptiveImageGlyph: AttributeScopes.SwiftUIAttributes.AdaptiveImageGlyphAttribute
}

TextEditor(text: $text)
    .attributedTextFormattingDefinition(MyAttributeScope.self)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/attributedtextformattingdefinition(_:)-8fwso)*