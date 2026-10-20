# init(id:for:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates the immersive space associated with an identifier for a specified type of presented data.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(id: String, for type: Data.Type, @ImmersiveSpaceContentBuilder content: @escaping (Binding<Data?>) -> Content)
```

**Other overloads**:

```swift
nonisolated
init<V>(id: String, for type: Data.Type, @ContentBuilder content: @escaping (Binding<Data?>) -> V) where Content == ImmersiveSpaceViewContent<V>, V : View
```

#### Discussion

The space uses the specified content builder to form the content. Your app invokes this initializer when it presents a value of the specified `type` using the [`openImmersiveSpace`](../environmentvalues/openimmersivespace.md) action.

## Parameters

- `id`: A string that uniquely identifies the immersive space. Ensure that identifiers are unique among the immersive spaces in your app.
- `type`: The type of presented data this immersive space accepts.
- `content`: An immersive space content builder that defines the content for each instance of the immersive space. The closure receives a binding to the value that you pass to the [`openImmersiveSpace`](../environmentvalues/openimmersivespace.md) action when you call that action to open an immersive space. The system automatically persists and restores the value of this binding during state restoration.

## See Also

### Creating a data-driven immersive space
- [init(for:content:)](./init%28for,content%29.md)
  Creates the immersive space for a specified type of presented data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersivespace/init(id:for:content:))*