# setEntry(_:for:)

**Framework**: Network  
**Kind**: method

Sets an entry in a TXT record dictionary.

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
@discardableResult
mutating func setEntry(_ entry: NWTXTRecord.Entry, for key: String) -> Bool
```

## See Also

- [init([String : String])](nwtxtrecord/init(_:)-566pd.md)
  Initializes a TXT record with a dictionary of strings.
- [func removeEntry(key: String) -> Bool](nwtxtrecord/removeentry(key:).md)
  Removes an entry from a TXT record dictionary.
- [NWTXTRecord.Entry](nwtxtrecord/entry.md)
  A type of entry in a TXT record dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwtxtrecord/setentry(_:for:))*