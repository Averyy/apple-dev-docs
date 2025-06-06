# dictionaryRepresentation

**Framework**: Foundation  
**Kind**: property

A dictionary containing all of the key-value pairs in the key-value store.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var dictionaryRepresentation: [String : Any] { get }
```

#### Discussion

This method returns the in-memory version of the keys and values. If you want to ensure that this dictionary contains the most recent set of changes, call [`synchronize()`](nsubiquitouskeyvaluestore/synchronize().md) shortly before calling this method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/dictionaryrepresentation)*