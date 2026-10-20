# NWTXTRecord.Entry

**Framework**: Network  
**Kind**: enum  
**Role**: Enumeration

A type of entry in a TXT record dictionary.

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
enum Entry
```

## Topics

### Entry Types
- [NWTXTRecord.Entry.none](./entry/none.md)
  The key is not mapped to any value.
- [NWTXTRecord.Entry.empty](./entry/empty.md)
  The key is mapped to an empty value.
- [NWTXTRecord.Entry.string(_:)](./entry/string%28_%29.md)
  The key is mapped to a string.
### Enumeration Cases
- [NWTXTRecord.Entry.data(_:)](./entry/data%28_%29.md)
### Initializers
- [init(Data?)](./entry/init%28_%29.md)
### Instance Properties
- [var data: Data?](./entry/data.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating TXT Records
- [init([String : String])](./init%28_%29-566pd.md)
  Initializes a TXT record with a dictionary of strings.
- [func removeEntry(key: String) -> Bool](./removeentry%28key%29.md)
  Removes an entry from a TXT record dictionary.
- [func setEntry(NWTXTRecord.Entry, for: String) -> Bool](./setentry%28_,for%29.md)
  Sets an entry in a TXT record dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwtxtrecord/entry)*