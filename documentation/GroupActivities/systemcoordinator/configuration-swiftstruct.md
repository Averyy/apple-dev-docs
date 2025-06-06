# SystemCoordinator.Configuration

**Framework**: Group Activities  
**Kind**: struct

A structure that specifies your app’s support for activities that take place in a shared simulation space.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct Configuration
```

#### Overview

A [`SystemCoordinator.Configuration`](systemcoordinator/configuration-swift.struct.md) structure stores your app’s preferences for the creation and arrangement of spatial Personas in a FaceTime call. Use this type to tell the system that you support activities that take place in one of your app’s immersive spaces, and how you want the system to arrange spatial Personas around your app’s content. To create a shared simulation space for your activity, set the [`supportsGroupImmersiveSpace`](systemcoordinator/configuration-swift.struct/supportsgroupimmersivespace.md) property to `true`.

To specify your app’s preferences, create a new [`SystemCoordinator.Configuration`](systemcoordinator/configuration-swift.struct.md) structure with those preferences and assign it to the [`configuration`](systemcoordinator/configuration-swift.property.md) property of your [`SystemCoordinator`](systemcoordinator.md) object. Assign this value before you join the session for the activity.

## Topics

### Creating a configuration structure
- [init()](systemcoordinator/configuration-swift.struct/init.md)
  Creates the type you use to specify your app’s preferences for shared contexts.
### Specifying spatial position preferences
- [var spatialTemplatePreference: SpatialTemplatePreference](systemcoordinator/configuration-swift.struct/spatialtemplatepreference.md)
  The preferred arrangement of spatial Personas in your app’s immersive space.
- [struct SpatialTemplatePreference](spatialtemplatepreference.md)
  A structure that specifies the preferred arrangement of participant spatial Personas in a shared simulation space.
### Supporting activities in immersive spaces
- [var supportsGroupImmersiveSpace: Bool](systemcoordinator/configuration-swift.struct/supportsgroupimmersivespace.md)
  A Boolean value that indicates whether your app supports a shared context when an immersive space is open.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [var configuration: SystemCoordinator.Configuration](systemcoordinator/configuration-swift.property.md)
  The current configuration of the system coordinator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/systemcoordinator/configuration-swift.struct)*