# SpatialTemplateConfiguration

**Framework**: Group Activities  
**Kind**: struct

A type that contains the configuration details for a spatial template.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct SpatialTemplateConfiguration
```

#### Overview

Create a [`SpatialTemplateConfiguration`](spatialtemplateconfiguration.md) structure and fill it with the information you want to apply to your custom [`SpatialTemplate`](spatialtemplate.md) type. A configuration structure contains the role to give to the person who initiates an activity that uses the template. For example, you might assign a presenter role to a person presenting a slide deck. Spatial templates use roles to place spatial Personas in the shared coordinate space.

## Topics

### Operators
- [static func == (SpatialTemplateConfiguration, SpatialTemplateConfiguration) -> Bool](spatialtemplateconfiguration/==(_:_:).md)
  Returns a Boolean value that indicates whether two values are equal.
### Initializers
- [init(defaultInitiatorRole: (any SpatialTemplateRole)?)](spatialtemplateconfiguration/init(defaultinitiatorrole:).md)
  Creates the configuration structure for a spatial template.
### Instance Properties
- [let defaultInitiatorRole: (any SpatialTemplateRole)?](spatialtemplateconfiguration/defaultinitiatorrole.md)
  The default role to assign to the initiator of the group activity.
- [var hashValue: Int](spatialtemplateconfiguration/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](spatialtemplateconfiguration/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](spatialtemplateconfiguration/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var configuration: SpatialTemplateConfiguration](spatialtemplate/configuration.md)
  Information a spatial template uses to configure itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/spatialtemplateconfiguration)*