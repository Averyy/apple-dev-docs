# Entity

**Framework**: RealityKit  
**Kind**: class

An element of a RealityKit scene to which you attach components that provide appearance and behavior characteristics for the entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency class Entity
```

## Mentions

- [Loading Reality Composer files manually without generated code](loading-reality-composer-files-manually-without-generated-code.md)
- [Improving the Accessibility of RealityKit Apps](improving-the-accessibility-of-realitykit-apps.md)
- [Arranging elements in a scene](arranging-elements-in-a-scene.md)
- [Manipulating Reality Composer scenes from code](manipulating-reality-composer-scenes-from-code.md)
- [Adding interactivity to behaviors](adding-interactivity-to-behaviors.md)

#### Overview

You create and configure entities to embody objects that you want to place in the real world in an AR app. You do this by adding [`Entity`](entity.md) instances to the [`Scene`](scene.md) instance associated with an [`ARView`](arview.md).

RealityKit defines a few concrete subclasses of [`Entity`](entity.md) that provide commonly used functionality. For example, you typically start by creating an instance of [`AnchorEntity`](anchorentity.md) to anchor your content, and add the anchor to a scene’s [`anchors`](scene/anchors.md) collection. You might then instantiate a [`ModelEntity`](modelentity.md) to represent a physical object in the scene, and add that as a child entity to the anchor. You can also create custom entities, and add them either to an anchor, or as children of another entity.

![Block diagram showing how entity hierarchies, composed of different kinds](https://docs-assets.developer.apple.com/published/1dd45148e6b513f8be6c51d113384e59/Entity-1%402x.png)

You can load predefined entities or a hierarchy of entities from your app’s bundle, or from a file on disk, using the methods in [`Stored entities`](stored-entities.md). Alternatively, you can create entities programmatically.

Entities contain components (instances conforming to the [`Component`](component.md) protocol) that provide appearance and behaviors for the entity. For example, the [`Transform`](transform.md) component contains the scale, rotation, and translation information needed to position an entity in space. You store components in the entity’s [`components`](entity/components.md) collection, which can hold exactly one of any component type. It makes sense to have only a single [`Transform`](transform.md) component, one [`ModelComponent`](modelcomponent.md) (specifying the visual appearance of the entity), and so on.

![Diagram showing the components present in the base entity class, as well](https://docs-assets.developer.apple.com/published/49fe65cf08e611d8df83f5f842db7f4a/Entity-2%402x.png)

All entities inherit a few common components from the [`Entity`](entity.md) base class: the [`Transform`](transform.md) component for spatial positioning, and [`SynchronizationComponent`](synchronizationcomponent.md), which enables synchronization of the entity among networked peers. Specific types of entities define additional behaviors. For example, the model entity has components for visual appearance ([`ModelComponent`](modelcomponent.md)), collision detection ([`CollisionComponent`](collisioncomponent.md)), and physics simulations ([`PhysicsBodyComponent`](physicsbodycomponent.md) and [`PhysicsMotionComponent`](physicsmotioncomponent.md)).

## Topics

### Creating an entity
- [init()](entity/init.md)
  Creates a new entity.
- [convenience init<each T>(components: repeat each T)](entity/init(components:)-80z41.md)
  Creates an entity with one or multiple components.
- [convenience init(components: [any Component])](entity/init(components:)-41rn1.md)
  Creates an entity with multiple components.
- [func clone(recursive: Bool) -> Self](entity/clone(recursive:).md)
  Duplicates an entity to create a new entity.
- [func didClone(from: Entity)](entity/didclone(from:).md)
  Tells a newly cloned entity that cloning is complete.
### Loading an entity from a file
- [Loading entities from a file](loading-entities-from-a-file.md)
  Retrieve an entity from storage on disk using a synchronous or an asynchronous load operation.
- [Stored entities](stored-entities.md)
  Manage entities that you store as assets on disk.
- [Creating USD files for Apple devices](creating-usd-files-for-apple-devices.md)
  Generate 3D assets that render as expected.
- [convenience(contentsOf:withName:)](entity/init(contentsof:withname:).md)
  Creates an entity by asynchronously loading it from a file URL.
- [convenience(named:in:)](entity/init(named:in:).md)
  Creates an entity by asynchronously loading it from a bundle.
- [struct ReferenceComponent](referencecomponent.md)
  A component that can load another entity from a file.
### Loading an entity from a configuration catalog
- [convenience(from:configurations:)](entity/init(from:configurations:).md)
  Loads an entity from a configuration catalog and a dictionary of configuration choices.
### Positioning entities in space
- [protocol HasTransform](hastransform.md)
  An interface that enables manipulating the scale, rotation, and translation of an entity.
- [struct Transform](transform.md)
  A component that defines the scale, rotation, and translation of an entity.
- [func transformMatrix(relativeTo: Entity.CoordinateSpaceReference) -> float4x4?](entity/transformmatrix(relativeto:).md)
  Returns the 4 x 4 transform matrix of an entity relative to the given coordinate space.
- [Entity.CoordinateSpaceReference](entity/coordinatespacereference.md)
  Defines the coordinate space reference for transform conversion.
### Relating entities
- [Entity.ChildCollection](entity/childcollection.md)
  A collection of child entities.
- [protocol HasHierarchy](hashierarchy.md)
  An interface that provides access to a parent entity and child entities.
### Managing components
- [var components: Entity.ComponentSet](entity/components.md)
  All the components that an entity stores.
- [Entity.ComponentSet](entity/componentset.md)
  A collection of components that an entity stores.
### Inspecting an entity
- [var scene: Scene?](entity/scene.md)
  The scene that owns the entity.
- [var name: String](entity/name.md)
  The name of the entity.
- [func findEntity(named: String) -> Entity?](entity/findentity(named:).md)
  Recursively searches all descendant entities for one with the given name.
- [var debugDescription: String](entity/debugdescription.md)
  A human readable description of the entity.
### Managing the entity’s state
- [var isEnabled: Bool](entity/isenabled.md)
  A Boolean that you set to enable or disable the entity and its descendants.
- [var isEnabledInHierarchy: Bool](entity/isenabledinhierarchy.md)
  A Boolean that indicates whether the entity and all of its ancestors are enabled.
- [var isActive: Bool](entity/isactive.md)
  A Boolean that indicates whether the entity is active.
- [var isAnchored: Bool](entity/isanchored.md)
  A Boolean that indicates whether the entity is anchored.
### Finding the nearest anchor
- [var anchor: (any HasAnchoring)?](entity/anchor.md)
  The nearest ancestor entity that can act as an anchor.
### Creating a collision shape
- [func generateCollisionShapes(recursive: Bool)](entity/generatecollisionshapes(recursive:).md)
  Creates the shape used to detect collisions between two entities that have collision components.
- [func generateCollisionShapes(recursive:static:)](entity/generatecollisionshapes(recursive:static:).md)
  Creates the shape used to detect collisions between two entities that have collision components.
### Animating an entity
- [var availableAnimations: [AnimationResource]](entity/availableanimations.md)
  The list of animations associated with the entity.
- [func playAnimation(_:transitionDuration:blendLayerOffset:separateAnimatedValue:startsPaused:clock:)](entity/playanimation(_:transitionduration:blendlayeroffset:separateanimatedvalue:startspaused:clock:).md)
  Plays an animation with the specified options.
- [func playAnimation(_:transitionDuration:blendLayerOffset:separateAnimatedValue:startsPaused:clock:handoffType:)](entity/playanimation(_:transitionduration:blendlayeroffset:separateanimatedvalue:startspaused:clock:handofftype:).md)
  Plays an animation with the specified options.
- [func playAnimation(AnimationResource, transitionDuration: TimeInterval, startsPaused: Bool) -> AnimationPlaybackController](entity/playanimation(_:transitionduration:startspaused:).md)
  Plays the given animation on the entity.
- [func stopAllAnimations(recursive: Bool)](entity/stopallanimations(recursive:).md)
  Stops all playing of animations on this entity.
- [struct ParameterSet](parameterset.md)
  A reference to general-purpose entity parameters for animations.
- [func playAnimation(named: String, transitionDuration: TimeInterval, startsPaused: Bool, recursive: Bool) -> AnimationPlaybackController](entity/playanimation(named:transitionduration:startspaused:recursive:).md)
  Plays all the animations with the given name on the entity.
- [subscript(_:)](entity/subscript(_:).md)
  Resolves the entity from the given entity path.
### Animating and controlling characters
- [func moveCharacter(by:deltaTime:relativeTo:collisionHandler:)](entity/movecharacter(by:deltatime:relativeto:collisionhandler:).md)
  Moves the character along a specified vector over a period of time.
- [func teleportCharacter(to:relativeTo:)](entity/teleportcharacter(to:relativeto:).md)
  Moves the character instantly to a new position.
### Playing audio
- [func playAudio(AudioResource) -> AudioPlaybackController](entity/playaudio(_:).md)
  Prepares and plays a new audio playback instance on this entity.
- [func playAudio(configuration:_:)](entity/playaudio(configuration:_:).md)
  Prepares and plays a real-time audio playback instance.
- [func prepareAudio(configuration:_:)](entity/prepareaudio(configuration:_:).md)
  Prepares a real-time audio playback instances.
- [func prepareAudio(AudioResource) -> AudioPlaybackController](entity/prepareaudio(_:).md)
  Prepares an audio resource for playback.
- [func stopAllAudio()](entity/stopallaudio.md)
  Stops playback for all audio on this entity.
### Saving an entity and its descendants
- [func write(to:)](entity/write(to:).md)
  Exports the entity as a RealityKit file to a location in the file system.
### Configuring accessibility features
- [Improving the Accessibility of RealityKit Apps](improving-the-accessibility-of-realitykit-apps.md)
  Incorporate assistive technologies in your augmented reality app.
- [var isAccessibilityElement: Bool](entity/isaccessibilityelement.md)
  A Boolean value indicating whether the receiver is an accessibility element that an assistive application can access.
- [var accessibilityDescription: String?](entity/accessibilitydescription.md)
  A longer description of the entity for use by assistive technologies.
- [var accessibilityLabel: String?](entity/accessibilitylabel.md)
  A succinct label that identifies the purpose of the image.
- [var accessibilityDescription: String?](entity/accessibilitydescription.md)
  A longer description of the entity for use by assistive technologies.
### Comparing entities
- [static func == (Entity, Entity) -> Bool](entity/==(_:_:).md)
  Indicates whether two entities are equal.
- [func hash(into: inout Hasher)](entity/hash(into:).md)
  Hashes the essential components of the entity by feeding them into the given hash function.
### Structures
- [Entity.ConfigurationCatalog](entity/configurationcatalog-1b69q.md)
  A collection of alternative representations of an entity you can choose from.
- [Entity.ConfigurationCatalog](entity/configurationcatalog-2tett.md)
  A collection of alternative representations of an entity you can choose from.
- [Entity.Observable](entity/observable-7cnpn.md)
  When properties in `Entity.Observable` are accessed, they participate in Observation. This means that when they change, any observers will be notified. Each of its properties passes through to the underlying Entity’s corresponding properties, so modifications of them will modify the underlying Entity’s corresponding property.
- [Entity.Observable](entity/observable-7ksgz.md)
  When properties in `Entity.Observable` are accessed, they participate in Observation. This means that when they change, any observers will be notified. Each of its properties passes through to the underlying Entity’s corresponding properties, so modifications of them will modify the underlying Entity’s corresponding property.
- [Entity.ParameterSet](entity/parameterset-3cp4c.md)
  Represents a reference to the parameters for a particular entity.
- [Entity.ParameterSet](entity/parameterset-49a5j.md)
  Represents a reference to the parameters for a particular entity.
### Initializers
- [convenience(components:)](entity/init(components:).md)
  Creates an entity with multiple components.
- [convenience(from:named:)](entity/init(from:named:).md)
  Creates an entity by asynchronously loading it from the in-memory contents of a file stored in a Data object.
### Instance Properties
- [var accessibilityCustomActions: [LocalizedStringResource]](entity/accessibilitycustomactions-3z61l.md)
  An array of custom actions supported by the entity, identified by their localized string key.
- [var accessibilityCustomActions: [LocalizedStringResource]](entity/accessibilitycustomactions-4yn75.md)
  An array of custom actions supported by the entity, identified by their localized string key.
- [var accessibilityCustomContent: [AccessibilityComponent.CustomContent]](entity/accessibilitycustomcontent-2tecl.md)
  The Custom Content API is useful for delivering accessibility information from complex data sets to your users in measured portions. Using this API allows you to leverage assistive technologies to present only the accessible content your app’s users need, when they need it.
- [var accessibilityCustomContent: [AccessibilityComponent.CustomContent]](entity/accessibilitycustomcontent-6gord.md)
  The Custom Content API is useful for delivering accessibility information from complex data sets to your users in measured portions. Using this API allows you to leverage assistive technologies to present only the accessible content your app’s users need, when they need it.
- [var accessibilityCustomRotors: [AccessibilityComponent.RotorType]](entity/accessibilitycustomrotors-2es9d.md)
  An array of supported rotors.
- [var accessibilityCustomRotors: [AccessibilityComponent.RotorType]](entity/accessibilitycustomrotors-5c8u0.md)
  An array of supported rotors.
- [var accessibilityLabelKey: LocalizedStringResource?](entity/accessibilitylabelkey-9va24.md)
  A succinct label that identifies the entity, in a localized string key.
- [var accessibilityLabelKey: LocalizedStringResource?](entity/accessibilitylabelkey-huzj.md)
  A succinct label that identifies the entity, in a localized string key.
- [var accessibilitySystemActions: AccessibilityComponent.SupportedActions](entity/accessibilitysystemactions-6i5a4.md)
  The set of supported accessibility actions.
- [var accessibilitySystemActions: AccessibilityComponent.SupportedActions](entity/accessibilitysystemactions-99mdm.md)
  The set of supported accessibility actions.
- [var accessibilityTraits: UIAccessibilityTraits](entity/accessibilitytraits-7v006.md)
  The combination of accessibility traits that best characterize the entity.
- [var accessibilityTraits: UIAccessibilityTraits](entity/accessibilitytraits-89wkv.md)
  The combination of accessibility traits that best characterize the entity.
- [var accessibilityValue: LocalizedStringResource?](entity/accessibilityvalue-29224.md)
  A localized string key that represents the current value of the entity.
- [var accessibilityValue: LocalizedStringResource?](entity/accessibilityvalue-2p0p.md)
  A localized string key that represents the current value of the entity.
- [var ambientAudio: AmbientAudioComponent?](entity/ambientaudio-3aad1.md)
  The component that configures the ambient rendering of sounds from this entity.
- [var ambientAudio: AmbientAudioComponent?](entity/ambientaudio-9eu19.md)
  The component that configures the ambient rendering of sounds from this entity.
- [var bindableValues: BindableValuesReference](entity/bindablevalues-36jjt.md)
- [var bindableValues: BindableValuesReference](entity/bindablevalues-9359q.md)
- [var channelAudio: ChannelAudioComponent?](entity/channelaudio-1esoy.md)
  The component that configures the channel-based rendering of sounds from this entity.
- [var channelAudio: ChannelAudioComponent?](entity/channelaudio-3pq7a.md)
  The component that configures the channel-based rendering of sounds from this entity.
- [var characterController: CharacterControllerComponent?](entity/charactercontroller-6q3oq.md)
  The character controller component for the entity.
- [var characterController: CharacterControllerComponent?](entity/charactercontroller-nc8x.md)
  The character controller component for the entity.
- [var characterControllerState: CharacterControllerStateComponent?](entity/charactercontrollerstate-5m5t3.md)
  The character controller state for  the entity.
- [var characterControllerState: CharacterControllerStateComponent?](entity/charactercontrollerstate-63sku.md)
  The character controller state for  the entity.
- [var defaultAnimationClock: CMClockOrTimebase](entity/defaultanimationclock-1w45z.md)
  Returns the default animation clock for this entity.
- [var defaultAnimationClock: CMClockOrTimebase](entity/defaultanimationclock-255so.md)
  Returns the default animation clock for this entity.
- [var observable: Entity.Observable](entity/observable-86yav.md)
- [var observable: Entity.Observable](entity/observable-9y2fi.md)
- [var parameters: Entity.ParameterSet](entity/parameters-5vkmj.md)
  Represents a reference to the parameters for a particular entity.
- [var parameters: Entity.ParameterSet](entity/parameters-87wyy.md)
  Represents a reference to the parameters for a particular entity.
- [var pins: EntityGeometricPins](entity/pins-26zc1.md)
  The entity’s geometric pins.
- [var pins: EntityGeometricPins](entity/pins-8mqgz.md)
  The entity’s geometric pins.
- [var spatialAudio: SpatialAudioComponent?](entity/spatialaudio-608d4.md)
  The component that configures the spatial rendering of sounds from this entity.
- [var spatialAudio: SpatialAudioComponent?](entity/spatialaudio-8w0hp.md)
  The component that configures the spatial rendering of sounds from this entity.
### Instance Methods
- [func applyTapForBehaviors()](entity/applytapforbehaviors.md)
  Apply a tap to an Entity or one of its ancestors to trigger a RealityComposer behavior if one is present.
- [func attach(_:to:)](entity/attach(_:to:).md)
  Attach an entity to a target pin owned by another entity with an optional specified source pin This utility function has the same effect of adding an AttachedTransformComponent created with the same parameter to the entity you are calling upon
### Type Methods
- [static func animate(Animation, body: () -> Void, completion: (() -> Void)?)](entity/animate(_:body:completion:).md)
### Enumerations
- [Entity.ForwardDirection](entity/forwarddirection-2osh9.md)
  Defines the forward direction for an entity.
- [Entity.ForwardDirection](entity/forwarddirection-5ji2e.md)
  Defines the forward direction for an entity.
### Default Implementations
- [CustomDebugStringConvertible Implementations](entity/customdebugstringconvertible-implementations.md)
- [Equatable Implementations](entity/equatable-implementations.md)
- [Hashable Implementations](entity/hashable-implementations.md)

## Relationships

### Inherited By
- [AnchorEntity](anchorentity.md)
- [BodyTrackedEntity](bodytrackedentity.md)
- [DirectionalLight](directionallight.md)
- [HasAnchoring](hasanchoring.md)
- [HasHierarchy](hashierarchy.md)
- [HasPhysicsMotion](hasphysicsmotion.md)
- [HasSceneUnderstanding](hassceneunderstanding.md)
- [HasSynchronization](hassynchronization.md)
- [HasTransform](hastransform.md)
- [ModelEntity](modelentity.md)
- [PerspectiveCamera](perspectivecamera.md)
- [PointLight](pointlight.md)
- [SpotLight](spotlight.md)
- [TriggerVolume](triggervolume.md)
- [ViewAttachmentEntity](viewattachmententity.md)
### Conforms To
- [CoordinateSpace3D](../Spatial/CoordinateSpace3D.md)
- [CoordinateSpace3DFloat](../Spatial/CoordinateSpace3DFloat.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [EventSource](eventsource.md)
- [HasHierarchy](hashierarchy.md)
- [HasSynchronization](hassynchronization.md)
- [HasTransform](hastransform.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Observable](../Observation/Observable.md)
- [RealityCoordinateSpace](realitycoordinatespace.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Understanding the modular architecture of RealityKit](../visionOS/understanding-the-realitykit-modular-architecture.md)
  Learn how everything fits together in RealityKit.
- [Building an immersive experience with RealityKit](building-an-immersive-experience-with-realitykit.md)
  Use systems and postprocessing effects to create a realistic underwater scene.
- [protocol Component](component.md)
  A representation of a geometry or a behavior that you apply to an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity)*