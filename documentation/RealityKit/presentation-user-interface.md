# Presentation UI

**Framework**: RealityKit

Control your app’s content and how people can interact with it.

#### Overview

RealityKit provides controls that enable interactions specific to each platform and context. For example, you can allow someone to interact with an entity that already has a [`CollisionComponent`](collisioncomponent.md) by adding the [`InputTargetComponent`](inputtargetcomponent.md) component. A RealityKit entity can visibly change when someone looks directly at it with a [`HoverEffectComponent`](hovereffectcomponent.md) component. Additionally, you can manage an entity’s accessibility information with [`AccessibilityComponent`](accessibilitycomponent.md).

## Topics

### Direct and indirect gestures
- [Transforming RealityKit entities using gestures](transforming-realitykit-entities-with-gestures.md)
  Build a RealityKit component to support standard visionOS gestures on any entity.
- [struct InputTargetComponent](inputtargetcomponent.md)
  A component that gives an entity the ability to receive system input.
- [struct ManipulationComponent](manipulationcomponent.md)
  A component that adds fluid and immersive interactive behaviors and effects.
- [struct GestureComponent](gesturecomponent.md)
- [struct EntityTargetValue](entitytargetvalue.md)
  A value containing an original gesture value along with a targeted entity.
### Accessibility
- [Improving the Accessibility of RealityKit Apps](improving-the-accessibility-of-realitykit-apps.md)
  Incorporate assistive technologies in your augmented reality app.
- [struct AccessibilityComponent](accessibilitycomponent.md)
  A component that stores accessibility information for an entity.
- [AccessibilityComponent.SupportedActions](accessibilitycomponent/supportedactions.md)
  A custom action that can be invoked on an entity in response to specific user cues.
- [AccessibilityComponent.CustomContent](accessibilitycomponent/customcontent-swift.struct.md)
  A CustomContent struct contains the accessibility strings for the labels you apply to your accessibility content.
- [AccessibilityComponent.RotorType](accessibilitycomponent/rotortype.md)
  A context-sensitive event that helps VoiceOver users find the next instance of a related element.
- [enum AccessibilityEvents](accessibilityevents.md)
### Visual adjustments
- [struct HoverEffectComponent](hovereffectcomponent.md)
  A component that applies a visual effect to a hierarchy of entities when a person looks at or selects an entity.
- [struct BillboardComponent](billboardcomponent.md)
  A component that orients an entity instance so that it continuously points toward the active camera.
- [struct EnvironmentBlendingComponent](environmentblendingcomponent.md)
  A component which controls how an entity will blend visually with objects in the user’s local environment
- [struct LensDistortionData](lensdistortiondata.md)
  A description of estimated lens distortion that can be used to rectify images.
- [struct ImagePresentationComponent](imagepresentationcomponent.md)
  A component that supports general image presentation.
### UIKit and AppKit gestures
- [ARView.EntityGestures](arview/entitygestures.md)
  The set of possible entity gesture recognizers.
- [class EntityRotationGestureRecognizer](entityrotationgesturerecognizer.md)
  A gesture recognizer that uses rotation gestures involving two touches to rotate a given entity.
- [class EntityScaleGestureRecognizer](entityscalegesturerecognizer.md)
  A gesture recognizer that uses a pinch gesture to scale or zoom an entity.
- [class EntityTranslationGestureRecognizer](entitytranslationgesturerecognizer.md)
  A gesture recognizer that uses a pan gesture to move an entity.
- [protocol EntityGestureRecognizer](entitygesturerecognizer.md)
  A gesture recognizer that works on entities.

## See Also

- [Views and attachments](presentation-views-and-attachments.md)
  Bring RealityKit content into your app with views and renderers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/presentation-user-interface)*