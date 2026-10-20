# SpatialTemplateConfiguration

**Framework**: Group Activities  
**Kind**: struct  
**Role**: Structure

A type that contains the configuration details for a spatial template.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct SpatialTemplateConfiguration
```

#### Overview

Create a [`SpatialTemplateConfiguration`](./spatialtemplateconfiguration.md) structure and fill it with the information you want to apply to your custom [`SpatialTemplate`](./spatialtemplate.md) type. A configuration structure contains the role to give to the person who initiates an activity that uses the template. For example, you might assign a presenter role to a person presenting a slide deck. Spatial templates use roles to place spatial Personas in the shared coordinate space.

## Topics

### Operators
- [static func == (SpatialTemplateConfiguration, SpatialTemplateConfiguration) -> Bool](./spatialtemplateconfiguration/eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two values are equal.
### Initializers
- [init(defaultInitiatorRole: (any SpatialTemplateRole)?)](./spatialtemplateconfiguration/init%28defaultinitiatorrole%29.md)
  Creates the configuration structure for a spatial template.
### Instance Properties
- [let defaultInitiatorRole: (any SpatialTemplateRole)?](./spatialtemplateconfiguration/defaultinitiatorrole.md)
  The default role to assign to the initiator of the group activity.
### Instance Methods
- [func hash(into: inout Hasher)](./spatialtemplateconfiguration/hash%28into%29.md)
  Hashes the essential components of this value by feeding them into the given hasher.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring the spatial template
- [var configuration: SpatialTemplateConfiguration](./spatialtemplate/configuration.md)
  Information a spatial template uses to configure itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/spatialtemplateconfiguration)*