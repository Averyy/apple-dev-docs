# subscript(_:)

**Framework**: Network  
**Kind**: subscript

Get and set values in a TXT record dictionary, by keys.

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
subscript(key: String) -> String? { get set }
```

## See Also

- [func getEntry(for: String) -> NWTXTRecord.Entry?](nwtxtrecord/getentry(for:).md)
  Accesses an entry in a TXT record dictionary.
- [var dictionary: [String : String]](nwtxtrecord/dictionary.md)
  The TXT record as a dictionary of strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwtxtrecord/subscript(_:))*