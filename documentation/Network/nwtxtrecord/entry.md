# NWTXTRecord.Entry

**Framework**: Network  
**Kind**: enum

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
- [NWTXTRecord.Entry.none](nwtxtrecord/entry/none.md)
  The key is not mapped to any value.
- [NWTXTRecord.Entry.empty](nwtxtrecord/entry/empty.md)
  The key is mapped to an empty value.
- [NWTXTRecord.Entry.string(_:)](nwtxtrecord/entry/string(_:).md)
  The key is mapped to a string.
### Enumeration Cases
- [NWTXTRecord.Entry.data(_:)](nwtxtrecord/entry/data(_:).md)
### Initializers
- [init(Data?)](nwtxtrecord/entry/init(_:).md)
### Instance Properties
- [var data: Data?](nwtxtrecord/entry/data.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init([String : String])](nwtxtrecord/init(_:)-566pd.md)
  Initializes a TXT record with a dictionary of strings.
- [func removeEntry(key: String) -> Bool](nwtxtrecord/removeentry(key:).md)
  Removes an entry from a TXT record dictionary.
- [func setEntry(NWTXTRecord.Entry, for: String) -> Bool](nwtxtrecord/setentry(_:for:).md)
  Sets an entry in a TXT record dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwtxtrecord/entry)*