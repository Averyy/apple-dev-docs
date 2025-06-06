# preferredAIDList

**Framework**: ProximityReader  
**Kind**: property

The preferred Application Identifier (AID) or Registered Application Provider Identifier (RID).

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 17.0+

## Declaration

```swift
var preferredAIDList: [Data]
```

#### Discussion

An ordered list of valid binary data between 5 and 16 bytes representing the preferred AID or RID. Use the preferred AID or RID when completing transactions with co-badged cards - a  or  card is a payment card that supports two or more payment brands.

> **Note**: In iOS 16 and earlier, the framework only uses the first entry. In iOS 17 and later, the list can have up to four entries.

In iOS 16 and earlier, the framework only uses the first entry. In iOS 17 and later, the list can have up to four entries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardtransactionrequest/preferredaidlist)*