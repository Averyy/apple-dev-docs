# sessionID

**Framework**: Accessory Transport Extension  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A unique identifier for a feature on the paired accessory.

**Availability**:
- iOS 27.0+

## Declaration

```swift
var sessionID: UUID { get }
```

## Discussion

This value matches the [`sessionID`](../transportmessage/sessionid.md) of the messages that your transport extension receives for the feature. The system uses it for cryptographic operations and persists the value until the accessory unpairs.

## Default Implementations

### AccessoryFeatureSession Implementations
- [var sessionID: UUID](./sessionid-1qpen.md)
  A unique identifier for a feature on the paired accessory.

## See Also

### Accessing the session
- [var accessory: ASAccessory](./accessory.md)
  A reference to the accessory to which the session communicates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeaturesession/sessionid)*