# replaceSelection(_:with:)

**Framework**: Foundation  
**Kind**: method

Replace the selection with new attributed content.

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
mutating func replaceSelection(_ selection: inout AttributedTextSelection, with newContent: some AttributedStringProtocol)
```

#### Discussion

In the case the selection is an insertion point, the `newContent` gets inserted at the caret location and the caret is moved to after the new content.

In the case where the selection spans one or multiple characters, those characters are removed and the new content is inserted at location of the first selected character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/replaceselection(_:with:))*