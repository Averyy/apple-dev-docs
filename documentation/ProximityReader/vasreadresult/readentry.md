# VASReadResult.ReadEntry

**Framework**: ProximityReader  
**Kind**: struct

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
- [let customerVASData: Data?](vasreadresult/readentry/customervasdata.md)
  The encrypted content of the pass stored in Wallet, which contains the loyalty or reward pass identifier.
### Getting the status word
- [let status: VASReadResult.ReadEntry.Status](vasreadresult/readentry/status-swift.property.md)
  The status word that represents the outcome of the VAS read attempt for this reward pass.
- [VASReadResult.ReadEntry.Status](vasreadresult/readentry/status-swift.enum.md)
  Status words that indicate the possible read outcomes.
### Getting the entry ID
- [let id: String](vasreadresult/readentry/id-swift.property.md)
  The merchant identifier you used to retrieve the loyalty program information from Wallet.
### Type Aliases
- [VASReadResult.ReadEntry.ID](vasreadresult/readentry/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let entries: [VASReadResult.ReadEntry]](vasreadresult/entries.md)
  The list of loyalty reward card entries received from the customer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/vasreadresult/readentry)*