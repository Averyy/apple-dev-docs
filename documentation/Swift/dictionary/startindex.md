# startIndex

**Framework**: Swift  
**Kind**: property

The position of the first element in a nonempty dictionary.

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
var startIndex: Dictionary<Key, Value>.Index { get }
```

#### Discussion

If the collection is empty, `startIndex` is equal to `endIndex`.

> **Note**: Amortized O(1) if the dictionary does not wrap a bridged `NSDictionary`. If the dictionary wraps a bridged `NSDictionary`, the performance is unspecified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary/startindex)*