# init(content:)

**Framework**: SwiftUI  
**Kind**: init

Creates an immersive space.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
init(@ImmersiveSpaceContentBuilder content: @escaping () -> Content) where Data == Never
```

#### Discussion

The space uses the specified content builder to form the content.

## Parameters

- `content`: An immersive space content builder that defines the content   of the space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersivespace/init(content:))*