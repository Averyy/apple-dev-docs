# init(for:content:defaultValue:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an immersive space for a specified type of presented data and a default value if the data is not set.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<V>(for type: Data.Type = Data.self, @ContentBuilder content: @escaping (Binding<Data>) -> V, defaultValue: @escaping () -> Data) where Content == ImmersiveSpaceViewContent<V>, V : View
```

Available when `Content` conforms to `ImmersiveSpaceContent`, `Data` conforms to `Decodable`, `Data` conforms to `Encodable`, and `Data` conforms to `Hashable`.

**Other overloads**:

```swift
nonisolated
init(for type: Data.Type = Data.self, @ImmersiveSpaceContentBuilder content: @escaping (Binding<Data>) -> Content, defaultValue: @escaping () -> Data)
```

## Discussion

The immersive space uses the specified view as a template to form the content of the space. Your app invokes this initializer when it presents a value of the specified `type` using the [`openImmersiveSpace`](../environmentvalues/openimmersivespace.md) action.

## Parameters

- `type`: The type of presented data this immersive space accepts.
- `content`: A content builder that defines the content for each instance of the immersive space. The closure receives a binding to the value that you pass to the [`openImmersiveSpace`](../environmentvalues/openimmersivespace.md) action when you use it to open an immersive space. The system automatically persists and restores the value of this binding during state restoration.
- `defaultValue`: A closure that returns a value that SwiftUI presents when it doesn’t receive one from you, like when you call the [`openImmersiveSpace`](../environmentvalues/openimmersivespace.md) action without providing a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersivespace/init(for:content:defaultvalue:)-ndd8)*