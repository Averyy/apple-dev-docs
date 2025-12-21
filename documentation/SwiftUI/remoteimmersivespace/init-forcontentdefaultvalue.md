# init(for:content:defaultValue:)

**Framework**: SwiftUI  
**Kind**: init

Creates the remote immersive space for a specified type of presented data, and a default value, if the data is not set.

**Availability**:
- macOS 26.0+

## Declaration

```swift
nonisolated
init<C>(for type: Data.Type = Data.self, @CompositorContentBuilder content: @escaping (Binding<Data>) -> C, defaultValue: @escaping () -> Data) where Content == CompositorContentBuilder.Content<C>, C : CompositorContent
```

#### Discussion

The immersive space uses the specified content builder as a template to form the content of the space. Your app invokes this initializer when it presents a value of the specified `type` using the [`openImmersiveSpace`](environmentvalues/openimmersivespace.md) action.

## Parameters

- `type`: The type of presented data this immersive space accepts.
- `content`: An immersive space content builder that defines the content   for each instance of the immersive space. The closure receives a   binding to the value that you pass to the    action when you call that   action to open an immersive space. The system automatically persists   and restores the value of this binding during state restoration.
- `defaultValue`: A closure that returns a value that SwiftUI presents   when it doesn’t receive one from you, like when you call the    action without providing a   value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/remoteimmersivespace/init(for:content:defaultvalue:))*