# init(defaultInitiatorRole:)

**Framework**: Group Activities  
**Kind**: init

Creates the configuration structure for a spatial template.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
init(defaultInitiatorRole: (any SpatialTemplateRole)? = nil)
```

#### Return Value

An initialized configuration object.

## Parameters

- `defaultInitiatorRole`: The template-specific role to apply to   the person who initiates the activity. The specified role must   be present in the template. Specify   if you don’t want to   assign a specific role to the initiator of the activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/spatialtemplateconfiguration/init(defaultinitiatorrole:))*