# AccessoryTransportSession.DataEvent.plaintext(data:featureID:)

**Framework**: Accessory Transport Extension  
**Kind**: case

A data event that contains unencrypted data for a feature.

**Availability**:
- iOS 26.3+
- iPadOS 26.3+
- Mac Catalyst 26.3+

## Declaration

```swift
case plaintext(data: Data, featureID: String)
```

## Parameters

- `data`: The plaintext data to transmit to the accessory.
- `featureID`: An identifier for the feature that generates the data.

## See Also

- [AccessoryTransportSession.DataEvent.ciphertext(data:featureID:)](accessorytransportsession/dataevent/ciphertext(data:featureid:).md)
  A data event that contains encrypted data for a specific feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/dataevent/plaintext(data:featureid:))*