# didApplyChanges(instanceIdentifier:operationIdentifier:)

**Framework**: Spatial Preview  
**Kind**: method  
**Required**: Yes

Event emitted to the ChangelistDelegate indicating the end of a USD change

**Availability**:
- macOS 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
func didApplyChanges(instanceIdentifier: String, operationIdentifier: UInt64)
```

## Parameters

- `instanceIdentifier`: The Spatial Preview receiver instance making the change
- `operationIdentifier`: Multiple changes with the same operation identifier can be grouped together


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/usdpreviewsession/changelistdelegate/didapplychanges(instanceidentifier:operationidentifier:))*