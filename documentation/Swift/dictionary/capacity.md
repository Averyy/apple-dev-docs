# capacity

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

The total number of key-value pairs that the dictionary can contain without allocating new storage.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var capacity: Int { get }
```

Available when `Key` conforms to `Hashable`.

## See Also

### Inspecting a Dictionary
- [var isEmpty: Bool](./isempty.md)
  A Boolean value that indicates whether the dictionary is empty.
- [var count: Int](./count.md)
  The number of key-value pairs in the dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/capacity)*