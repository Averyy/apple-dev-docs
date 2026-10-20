# NWTXTRecord

**Framework**: Network  
**Kind**: struct  
**Role**: Structure

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
- [init([String : String])](./nwtxtrecord/init%28_%29-566pd.md)
  Initializes a TXT record with a dictionary of strings.
- [func removeEntry(key: String) -> Bool](./nwtxtrecord/removeentry%28key%29.md)
  Removes an entry from a TXT record dictionary.
- [func setEntry(NWTXTRecord.Entry, for: String) -> Bool](./nwtxtrecord/setentry%28_,for%29.md)
  Sets an entry in a TXT record dictionary.
- [NWTXTRecord.Entry](./nwtxtrecord/entry.md)
  A type of entry in a TXT record dictionary.
### Examining TXT Records
- [func getEntry(for: String) -> NWTXTRecord.Entry?](./nwtxtrecord/getentry%28for%29.md)
  Accesses an entry in a TXT record dictionary.
- [subscript(String) -> String?](./nwtxtrecord/subscript%28_%29.md)
  Get and set values in a TXT record dictionary, by keys.
- [var dictionary: [String : String]](./nwtxtrecord/dictionary.md)
  The TXT record as a dictionary of strings.
### Initializers
- [init(Data)](./nwtxtrecord/init%28_%29-30jy4.md)
- [init([String : Data])](./nwtxtrecord/init%28_%29-69q7g.md)
  Create an NWTXTRecord object from a Dictionary<String, Data>.
- [init([String : NWTXTRecord.Entry])](./nwtxtrecord/init%28_%29-7cww7.md)
  Create an NWTXTRecord object from a Dictionary<String, NWTXTRecord.Entry>.
### Instance Properties
- [var data: Data](./nwtxtrecord/data.md)
- [var dataDictionary: [String : Data]](./nwtxtrecord/datadictionary.md)
  Access the contents of an NWTXTRecord represented by a Dictionary<String, Data>.
- [var entries: [String : NWTXTRecord.Entry]](./nwtxtrecord/entries.md)
  Get all entries present in the TXT record.

## Relationships

### Conforms To
- [Collection](../Swift/collection.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Evaluating Browser Results
- [let endpoint: NWEndpoint](./nwbrowser/result/endpoint.md)
  The discovered service endpoint.
- [let interfaces: [NWInterface]](./nwbrowser/result/interfaces.md)
  The list of interfaces on which the service was discovered.
- [let metadata: NWBrowser.Result.Metadata](./nwbrowser/result/metadata-swift.property.md)
  The metadata associated with the discovered service, such as the TXT record.
- [NWBrowser.Result.Metadata](./nwbrowser/result/metadata-swift.enum.md)
  Values associated with discovered services, such as TXT records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwtxtrecord)*