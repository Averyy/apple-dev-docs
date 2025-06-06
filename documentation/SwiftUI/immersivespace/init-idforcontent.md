# init(id:for:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates the immersive space associated with an identifier for a specified type of presented data.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
init(id: String, for type: Data.Type, @ImmersiveSpaceContentBuilder content: @escaping (Binding<Data?>) -> Content)
```

#### Discussion

The space uses the specified content builder to form the content. Your app invokes this initializer when it presents a value of the specified `type` using the [`openImmersiveSpace`](environmentvalues/openimmersivespace.md) action.

## Parameters

- `id`: A string that uniquely identifies the immersive space. Ensure   that identifiers are unique among the immersive spaces in your app.
- `type`: The type of presented data this immersive space accepts.
- `content`: An immersive space content builder that defines the content   for each instance of the immersive space. The closure receives a   binding to the value that you pass to the    action when you call that   action to open an immersive space. The system automatically persists   and restores the value of this binding during state restoration.

## See Also

- [init(for:content:)](immersivespace/init(for:content:).md)
  Creates the immersive space for a specified type of presented data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersivespace/init(id:for:content:))*