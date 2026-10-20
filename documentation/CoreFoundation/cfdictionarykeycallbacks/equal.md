# equal

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Instance Property

The callback used to compare keys in the dictionary for equality. If `NULL`, the collection will use pointer equality to compare keys in the collection. See [`CFDictionaryEqualCallBack`](../cfdictionaryequalcallback.md) for a description of this callback.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var equal: CFDictionaryEqualCallBack!
```

```c
CFDictionaryEqualCallBack equal;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionarykeycallbacks/equal)*