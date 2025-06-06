# navigationDocument(_:)

**Framework**: RealityKit  
**Kind**: method

Configures the view’s document for purposes of navigation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func navigationDocument(_ url: URL) -> some View
```

#### Discussion

In iOS, iPadOS, this populates the title menu with a header previewing the document. In macOS, this populates a proxy icon.

Refer to the doc:Configure-Your-Apps-Navigation-Titles article for more information on navigation document modifiers.

## Parameters

- `document`: The URL content associated to the   navigation title.
- `preview`: The preview of the document to use when sharing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3d/navigationdocument(_:)-13rxz)*