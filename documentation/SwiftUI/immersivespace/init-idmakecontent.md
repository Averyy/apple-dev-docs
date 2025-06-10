# init(id:makeContent:)

**Framework**: SwiftUI  
**Kind**: init

Creates the immersive space associated with the specified identifier.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
init(id: String, @ImmersiveSpaceContentBuilder makeContent: @escaping () -> Content) where Data == Never
```

#### Discussion

The space uses the specified content builder to form the content.

## Parameters

- `id`: A string that uniquely identifies the immersive space. Ensure   that identifiers are unique among the immersive spaces in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersivespace/init(id:makecontent:))*