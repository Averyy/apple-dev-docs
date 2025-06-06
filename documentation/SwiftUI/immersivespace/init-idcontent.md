# init(id:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates the immersive space associated with the specified identifier.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
init(id: String, @ImmersiveSpaceContentBuilder content: () -> Content) where Data == Never
```

#### Discussion

The space uses the specified content builder to form the content.

## Parameters

- `id`: A string that uniquely identifies the immersive space. Ensure   that identifiers are unique among the immersive spaces in your app.
- `content`: An immersive space content builder that defines the content   of the space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersivespace/init(id:content:))*