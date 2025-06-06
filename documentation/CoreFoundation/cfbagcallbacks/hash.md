# hash

**Framework**: Core Foundation  
**Kind**: property

The callback used to compute a hash code for values in a collection. If `NULL`, the collection computes a hash code by converting the pointer value to an integer. See [`CFBagHashCallBack`](cfbaghashcallback.md) for a description of this callback.

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
var hash: CFBagHashCallBack!
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbagcallbacks/hash)*