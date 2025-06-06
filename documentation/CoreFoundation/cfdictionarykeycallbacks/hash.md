# hash

**Framework**: Core Foundation  
**Kind**: property

The callback used to compute a hash code for keys as they are used to access, add, or remove values in the dictionary. If `NULL`, the collection computes a hash code by converting the pointer value to an integer. See [`CFDictionaryHashCallBack`](cfdictionaryhashcallback.md) for a description of this callback.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var hash: CFDictionaryHashCallBack!
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionarykeycallbacks/hash)*