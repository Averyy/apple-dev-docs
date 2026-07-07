# willApplyChanges(instanceIdentifier:operationIdentifier:)

**Framework**: Spatial Preview  
**Kind**: method  
**Required**: Yes

An event emitted to the ChangeListDelegate indicating the start of a USD change.

**Availability**:
- macOS 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
func willApplyChanges(instanceIdentifier: String, operationIdentifier: UInt)
```

## Parameters

- `instanceIdentifier`: The Spatial Preview receiver instance making the change.
- `operationIdentifier`: Multiple changes with the same operation identifier can be grouped together.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/usdpreviewsession/changelistdelegate/willapplychanges(instanceidentifier:operationidentifier:))*