# sessionID

**Framework**: Accessory Transport Extension  
**Kind**: property  
**Role**: Instance Property

A unique identifier for a feature on the paired accessory.

**Availability**:
- iOS 27.0+

## Declaration

```swift
var sessionID: UUID { get }
```

## Discussion

This value matches the [`sessionID`](../transportmessage/sessionid.md) of the messages that your transport extension receives for the feature. The system uses it for cryptographic operations and persists the value until the accessory unpairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeaturesession/sessionid-1qpen)*