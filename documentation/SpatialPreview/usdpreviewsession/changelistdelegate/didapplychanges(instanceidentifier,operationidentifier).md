# didApplyChanges(instanceIdentifier:operationIdentifier:)

**Framework**: Spatial Preview  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

An event emitted to the ChangelistDelegate indicating the end of a USD change.

**Availability**:
- macOS 27.0+
- visionOS

## Declaration

```swift
@MainActor
func didApplyChanges(instanceIdentifier: String, operationIdentifier: UInt)
```

## Parameters

- `instanceIdentifier`: The Spatial Preview receiver instance making the change.
- `operationIdentifier`: Multiple changes with the same operation identifier can be grouped together.

## See Also

### Responding to changes
- [func willApplyChanges(instanceIdentifier: String, operationIdentifier: UInt)](./willapplychanges%28instanceidentifier,operationidentifier%29.md)
  An event emitted to the ChangeListDelegate indicating the start of a USD change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/usdpreviewsession/changelistdelegate/didapplychanges(instanceidentifier:operationidentifier:))*