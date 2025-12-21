# init(configuration:content:)

**Framework**: RealityKit  
**Kind**: init

Present `content` using modality and options specified by `configuration`. A component created using this method will have its `isPresented` property default to `true`, which means it will present as soon as an entity with the component is added to the hierarchy.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
nonisolated
init<Content>(configuration: PresentationComponent.Configuration, content: Content) where Content : View
```

#### Discussion

Use this component when you want to present a modal that is anchored to an entity. Listen to `ComponentEvents.DidChange` event to receive notification about the presentation’s dismissal. To control the presentation through a SwiftUI Binding, use `PresentationComponent(isPresented:configuration:content)`

## Parameters

- `configuration`: A configuration that specifies the modality,   appearance, and behavior of the presentation.
- `content`: The SwiftUI view hierarchy that you want to present with   the component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/presentationcomponent/init(configuration:content:))*