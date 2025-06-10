# init(isPresented:configuration:content:)

**Framework**: RealityKit  
**Kind**: init

Present `content` when a binding that you provide is `true`, using modality and options specified by `configuration`.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
init<Content>(isPresented: Binding<Bool>, configuration: PresentationComponent.Configuration, content: Content) where Content : View
```

#### Discussion

Use this component when you want to present a modal that is anchored to an entity.

## Parameters

- `isPresented`: A binding to a Boolean value that determines whether   to present the content.
- `configuration`: A configuration that specifies the modality,   appearance, and behavior of the presentation.
- `content`: The SwiftUI view hierarchy that you want to present with   the component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/presentationcomponent/init(ispresented:configuration:content:))*