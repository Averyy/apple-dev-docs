# VASReadResult.ReadEntry

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

An object containing encrypted data associated with a customer’s loyalty or reward pass.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
struct ReadEntry
```

## Topics

### Getting the customer data
- [let customerVASData: Data?](./readentry/customervasdata.md)
  The encrypted content of the pass stored in Wallet, which contains the loyalty or reward pass identifier.
### Getting the status word
- [let status: VASReadResult.ReadEntry.Status](./readentry/status-swift.property.md)
  The status word that represents the outcome of the VAS read attempt for this reward pass.
- [VASReadResult.ReadEntry.Status](./readentry/status-swift.enum.md)
  Status words that indicate the possible read outcomes.
### Getting the entry ID
- [let id: String](./readentry/id.md)
  The merchant identifier you used to retrieve the loyalty program information from Wallet.

## Relationships

### Conforms To
- [Identifiable](../../Swift/identifiable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the entry details
- [let entries: [VASReadResult.ReadEntry]](./entries.md)
  The list of loyalty reward card entries received from the customer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/vasreadresult/readentry)*