# NWTXTRecord

**Framework**: Network  
**Kind**: struct

A dictionary representing a TXT record in a DNS packet.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct NWTXTRecord
```

## Topics

### Creating TXT Records
- [init([String : String])](nwtxtrecord/init(_:)-566pd.md)
  Initializes a TXT record with a dictionary of strings.
- [func removeEntry(key: String) -> Bool](nwtxtrecord/removeentry(key:).md)
  Removes an entry from a TXT record dictionary.
- [func setEntry(NWTXTRecord.Entry, for: String) -> Bool](nwtxtrecord/setentry(_:for:).md)
  Sets an entry in a TXT record dictionary.
- [NWTXTRecord.Entry](nwtxtrecord/entry.md)
  A type of entry in a TXT record dictionary.
### Examining TXT Records
- [func getEntry(for: String) -> NWTXTRecord.Entry?](nwtxtrecord/getentry(for:).md)
  Accesses an entry in a TXT record dictionary.
- [subscript(String) -> String?](nwtxtrecord/subscript(_:).md)
  Get and set values in a TXT record dictionary, by keys.
- [var dictionary: [String : String]](nwtxtrecord/dictionary.md)
  The TXT record as a dictionary of strings.
### Initializers
- [init(Data)](nwtxtrecord/init(_:)-30jy4.md)
### Instance Properties
- [var data: Data](nwtxtrecord/data.md)

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [let endpoint: NWEndpoint](nwbrowser/result/endpoint.md)
  The discovered service endpoint.
- [let interfaces: [NWInterface]](nwbrowser/result/interfaces.md)
  The list of interfaces on which the service was discovered.
- [let metadata: NWBrowser.Result.Metadata](nwbrowser/result/metadata-swift.property.md)
  The metadata associated with the discovered service, such as the TXT record.
- [NWBrowser.Result.Metadata](nwbrowser/result/metadata-swift.enum.md)
  Values associated with discovered services, such as TXT records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwtxtrecord)*