# replaceSelection(_:withCharacters:)

**Framework**: Foundation  
**Kind**: method

Replace the selection with new content, attributed with the typing attributes.

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
mutating func replaceSelection(_ selection: inout AttributedTextSelection, withCharacters newContent: some Collection<Character>)
```

#### Discussion

Operates just like [`replaceSelection(_:with:)`](attributedstring/replaceselection(_:with:).md), but applies the typing attributes to the new content before inserting it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/replaceselection(_:withcharacters:))*