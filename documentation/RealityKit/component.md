# Component

**Framework**: RealityKit  
**Kind**: protocol

A representation of a geometry or a behavior that you apply to an entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
protocol Component
```

#### Overview

You assemble a particular combination of behavior and appearance for an entity by adding components to the [`components`](entity/components.md) set of an [`Entity`](entity.md) instance. Each component, represented by a type that conforms to the [`Component`](component.md) protocol, defines a single aspect of the entity. For example, one might define a position in space, while another provides a visual appearance. You can add at most one component of a given type to an entity.

![Diagram showing the components present in different kinds of](https://docs-assets.developer.apple.com/published/96d2fd3bd0efc9b6465eba71a243dbc7/Component-1%402x.png)

RealityKit has a variety of predefined component types that you can use to add commonly needed characteristics. For example, the [`ModelComponent`](modelcomponent.md) specifies visual appearance with a mesh and materials. The [`CollisionComponent`](collisioncomponent.md) contains a shape and other information used to decide if one entity collides with another.

You can also define custom component types. When you do, register that type with the system by calling the new component’s [`registerComponent()`](component/registercomponent().md) method—a default implementation of which is provided by the [`Component`](component.md) protocol. Call this method once before using the component type. You don’t need to make this call for component types that RealityKit provides.

> 💡 **Tip**: You can subscribe to [`ComponentEvents`](componentevents.md) for events that the system triggers when you interact with components.

## Topics

### Registering a component type
- [static func registerComponent()](component/registercomponent.md)
  Registers a new component type.

## Relationships

### Inherited By
- [TransientComponent](transientcomponent.md)
### Conforming Types
- [ARKitAnchorComponent](arkitanchorcomponent.md)
- [AccessibilityComponent](accessibilitycomponent.md)
- [AdaptiveResolutionComponent](adaptiveresolutioncomponent.md)
- [AmbientAudioComponent](ambientaudiocomponent.md)
- [AnchoringComponent](anchoringcomponent.md)
- [AnimationGraphComponent](animationgraphcomponent.md)
- [AnimationLibraryComponent](animationlibrarycomponent.md)
- [AttachedTransformComponent](attachedtransformcomponent.md)
- [AudioLibraryComponent](audiolibrarycomponent.md)
- [AudioMixGroupsComponent](audiomixgroupscomponent.md)
- [BehaviorTreeComponent](behaviortreecomponent.md)
- [BillboardComponent](billboardcomponent.md)
- [BlendShapeWeightsComponent](blendshapeweightscomponent.md)
- [BloomComponent](bloomcomponent.md)
- [BloomOptionsComponent](bloomoptionscomponent.md)
- [BodyTrackingComponent](bodytrackingcomponent.md)
- [ChannelAudioComponent](channelaudiocomponent.md)
- [CharacterControllerComponent](charactercontrollercomponent.md)
- [CharacterControllerStateComponent](charactercontrollerstatecomponent.md)
- [ClippingComponent](clippingcomponent.md)
- [ClothBodyComponent](clothbodycomponent.md)
- [ClothColliderComponent](clothcollidercomponent.md)
- [ClothForceVolumeComponent](clothforcevolumecomponent.md)
- [ClothGrabComponent](clothgrabcomponent.md)
- [ClothQueryVolumeComponent](clothqueryvolumecomponent.md)
- [ClothSimulationComponent](clothsimulationcomponent.md)
- [CollisionComponent](collisioncomponent.md)
- [ComputeGraphComponent](computegraphcomponent.md)
- [ComputeGraphOutputComponent](computegraphoutputcomponent.md)
- [ComputeGraphRuntimeComponent](computegraphruntimecomponent.md)
- [ComputeGraphSharedUniforms](computegraphshareduniforms.md)
- [ComputeGraphViewpointComponent](computegraphviewpointcomponent.md)
- [DiffuseLightProbeGroupComponent](diffuselightprobegroupcomponent.md)
- [DiffuseLightProbeReceiverComponent](diffuselightprobereceivercomponent.md)
- [DirectionalLightComponent](directionallightcomponent.md)
- [DirectionalLightComponent.Shadow](directionallightcomponent/shadow.md)
- [DockingRegionComponent](dockingregioncomponent.md)
- [DynamicLightShadowComponent](dynamiclightshadowcomponent.md)
- [EnvironmentBlendingComponent](environmentblendingcomponent.md)
- [EnvironmentLightingConfigurationComponent](environmentlightingconfigurationcomponent.md)
- [ForceEffectComponent](forceeffectcomponent.md)
- [GaussianSplatComponent](gaussiansplatcomponent.md)
- [GeometricPinsComponent](geometricpinscomponent.md)
- [GestureComponent](gesturecomponent.md)
- [GroundingShadowComponent](groundingshadowcomponent.md)
- [HoverEffectComponent](hovereffectcomponent.md)
- [IKComponent](ikcomponent.md)
- [ImageBasedLightComponent](imagebasedlightcomponent.md)
- [ImageBasedLightReceiverComponent](imagebasedlightreceivercomponent.md)
- [ImagePresentationComponent](imagepresentationcomponent.md)
- [InputTargetComponent](inputtargetcomponent.md)
- [LevelOfDetailComponent](levelofdetailcomponent.md)
- [LightmapComponent](lightmapcomponent.md)
- [ManipulationComponent](manipulationcomponent.md)
- [ManipulationComponent.HitTarget](manipulationcomponent/hittarget.md)
- [MeshDeformerComponent](meshdeformercomponent.md)
- [MeshInstancesComponent](meshinstancescomponent.md)
- [ModelComponent](modelcomponent.md)
- [ModelDebugOptionsComponent](modeldebugoptionscomponent.md)
- [ModelSortGroupComponent](modelsortgroupcomponent.md)
- [NavigationComponent](navigationcomponent.md)
- [NavigationMeshComponent](navigationmeshcomponent.md)
- [OcclusionCullingComponent](occlusioncullingcomponent.md)
- [OpacityComponent](opacitycomponent.md)
- [OrthographicCameraComponent](orthographiccameracomponent.md)
- [ParticleEmitterComponent](particleemittercomponent.md)
- [PerspectiveCameraComponent](perspectivecameracomponent.md)
- [PhysicallyBasedDecalComponent](physicallybaseddecalcomponent.md)
- [PhysicsBodyComponent](physicsbodycomponent.md)
- [PhysicsJointsComponent](physicsjointscomponent.md)
- [PhysicsMotionComponent](physicsmotioncomponent.md)
- [PhysicsSimulationComponent](physicssimulationcomponent.md)
- [PointLightComponent](pointlightcomponent.md)
- [PointLightComponent.SurroundingsLight](pointlightcomponent/surroundingslight.md)
- [PortalComponent](portalcomponent.md)
- [PortalCrossingComponent](portalcrossingcomponent.md)
- [PresentationComponent](presentationcomponent.md)
- [ProjectiveTransformCameraComponent](projectivetransformcameracomponent.md)
- [ReferenceComponent](referencecomponent.md)
- [RenderLayerComponent](renderlayercomponent.md)
- [ReverbComponent](reverbcomponent.md)
- [SceneUnderstandingComponent](sceneunderstandingcomponent.md)
- [SkeletalPosesComponent](skeletalposescomponent.md)
- [SpatialAudioComponent](spatialaudiocomponent.md)
- [SpotLightComponent](spotlightcomponent.md)
- [SpotLightComponent.ProjectiveTexture](spotlightcomponent/projectivetexture.md)
- [SpotLightComponent.Shadow](spotlightcomponent/shadow.md)
- [SpotLightComponent.SurroundingsLight](spotlightcomponent/surroundingslight.md)
- [SynchronizationComponent](synchronizationcomponent.md)
- [TextComponent](textcomponent.md)
- [ToneMappingComponent](tonemappingcomponent.md)
- [Transform](transform.md)
- [VideoPlayerComponent](videoplayercomponent.md)
- [ViewAttachmentComponent](viewattachmentcomponent.md)
- [VirtualEnvironmentProbeComponent](virtualenvironmentprobecomponent.md)
- [WorldComponent](worldcomponent.md)

## See Also

- [Understanding the modular architecture of RealityKit](../visionOS/understanding-the-realitykit-modular-architecture.md)
  Learn how everything fits together in RealityKit.
- [Building an immersive experience with RealityKit](building-an-immersive-experience-with-realitykit.md)
  Use systems and postprocessing effects to create a realistic underwater scene.
- [class Entity](entity.md)
  An element of a RealityKit scene to which you attach components that provide appearance and behavior characteristics for the entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/component)*