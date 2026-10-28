# init(id:for:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates the immersive space associated with an identifier for a specified type of presented data using view-based content.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<V>(id: String, for type: Data.Type, @ContentBuilder content: @escaping (Binding<Data?>) -> V) where Content == ImmersiveSpaceViewContent<V>, V : View
```

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to `Hashable`.

**Other overloads**:

```swift
nonisolated
init(id: String, for type: Data.Type, @ImmersiveSpaceContentBuilder content: @escaping (Binding<Data?>) -> Content)
```

## Discussion

The immersive space uses the specified view as a template to form the content of the space. Your app invokes this initializer when it presents a value of the specified `type` using the [`openImmersiveSpace`](../environmentvalues/openimmersivespace.md) action.

## Parameters

- `id`: A string that uniquely identifies the immersive space. Ensure that identifiers are unique among the immersive spaces in your app.
- `type`: The type of presented data this immersive space accepts.
- `content`: A content builder that defines the content for each instance of the immersive space. The closure receives a binding to the value that you pass to the [`openImmersiveSpace`](../environmentvalues/openimmersivespace.md) action when you use it to open an immersive space. The system automatically persists and restores the value of this binding during state restoration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersivespace/init(id:for:content:)-6i5bn)*