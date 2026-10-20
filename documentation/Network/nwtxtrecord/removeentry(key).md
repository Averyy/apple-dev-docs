# removeEntry(key:)

**Framework**: Network  
**Kind**: method  
**Role**: Instance Method

Removes an entry from a TXT record dictionary.

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
mutating func removeEntry(key: String) -> Bool
```

## See Also

### Creating TXT Records
- [init([String : String])](./init%28_%29-566pd.md)
  Initializes a TXT record with a dictionary of strings.
- [func setEntry(NWTXTRecord.Entry, for: String) -> Bool](./setentry%28_,for%29.md)
  Sets an entry in a TXT record dictionary.
- [NWTXTRecord.Entry](./entry.md)
  A type of entry in a TXT record dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwtxtrecord/removeentry(key:))*