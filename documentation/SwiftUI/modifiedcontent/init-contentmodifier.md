# init(content:modifier:)

**Framework**: SwiftUI  
**Kind**: init

A structure that defines the content and modifier needed to produce a new view or view modifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
init(content: Content, modifier: Modifier)
```

#### Discussion

If `content` is a [`View`](view.md) and `modifier` is a [`ViewModifier`](viewmodifier.md), the result is a [`View`](view.md). If `content` and `modifier` are both view modifiers, then the result is a new [`ViewModifier`](viewmodifier.md) combining them.

## Parameters

- `content`: The content that the modifier changes.
- `modifier`: The modifier to apply to the content.

## See Also

- [var content: Content](modifiedcontent/content.md)
  The content that the modifier transforms into a new view or new view modifier.
- [var modifier: Modifier](modifiedcontent/modifier.md)
  The view modifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/modifiedcontent/init(content:modifier:))*