# AccessoryTransportSession.DataEvent.ciphertext(data:featureID:)

**Framework**: Accessory Transport Extension  
**Kind**: case

A data event that contains encrypted data for a specific feature.

**Availability**:
- iOS 26.3+
- iPadOS 26.3+
- Mac Catalyst 26.3+

## Declaration

```swift
case ciphertext(data: Data, featureID: String)
```

## Parameters

- `data`: The encrypted data to transmit to the accessory.
- `featureID`: A string identifier for the feature that generated the data.

## See Also

- [AccessoryTransportSession.DataEvent.plaintext(data:featureID:)](accessorytransportsession/dataevent/plaintext(data:featureid:).md)
  A data event that contains unencrypted data for a feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/dataevent/ciphertext(data:featureid:))*