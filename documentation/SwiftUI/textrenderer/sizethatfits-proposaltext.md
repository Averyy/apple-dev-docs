# sizeThatFits(proposal:text:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Returns the size of the text in `proposal`. The provided `text` proxy value may be used to query the sizing behavior of the underlying text layout.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func sizeThatFits(proposal: ProposedViewSize, text: TextProxy) -> CGSize
```

#### Discussion

The default implementation of this function returns `text.size(proposal)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textrenderer/sizethatfits(proposal:text:))*