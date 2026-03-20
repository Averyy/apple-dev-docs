# sendData(_:featureID:)

**Framework**: Accessory Transport Extension  
**Kind**: method

Sends feature data to the system from the accessory.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
func sendData(_ data: Data, featureID: String) throws(AccessoryTransportSession.Error)
```

## Parameters

- `data`: The data to send to the accessory.
- `featureID`: An identifier for the feature to which the data relates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/senddata(_:featureid:))*