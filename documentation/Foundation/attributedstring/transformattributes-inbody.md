# transformAttributes(in:body:)

**Framework**: Foundation  
**Kind**: method

Apply a change to the attributes in the entire selection.

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
mutating func transformAttributes<E>(in selection: inout AttributedTextSelection, body: (inout AttributeContainer) throws(E) -> Void) throws(E) where E : Error
```

#### Discussion

Applies the given `body` to the selection. Specifically, in the case of a selection spanning one or multiple characters, the `body` is applied to every run in the selection individually, modifying only the part of the run that is in the selection.

In the case of an insertion point, the `body` is applied to the attribute container defining the typing attributes. After that, attributes that are bound to the whole paragraph or the character immediately preceding the caret via [`AttributedString.AttributeRunBoundaries`](AttributedString/AttributeRunBoundaries.md) are applied directly to attributed string at the respective range.

Use this function to implement controls that operate on the user’s current selection. Some controls define the new value relative to the current state of each individual run in the selection, e.g. a stepper for the font size:

```None
Stepper("Font Size", onIncrement: {
    text.transformAttributes(in: &selection) {
        $0.font = ($0.font ?? .default).scaled(by: 1.2)
    }
}, onDecrement: {
    text.transformAttributes(in: &selection) {
        $0.font = ($0.font ?? .default).scaled(by: 1 / 1.2)
    }
})
```

Other controls, such as toggles for boldness, italics, or underline usually define the new value for all ranges as the opposite of the value in the typing attributes, as defined by `AttributedTextSelection/typingAttributes(in:)`:

```None
Toggle("B", isOn: .init(get: {
    let font = selection.typingAttributes(in: text).font ?? .default
    return font.resolve(in: environment).isBold
}, set: { isBold in
    text.transformAttributes(in: &selection) {
        $0.font = ($0.font ?? .default).bold(isBold)
    }
}))
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/transformattributes(in:body:))*