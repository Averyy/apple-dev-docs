# listElementID

**Framework**: MediaExtension  
**Kind**: property

A unique number in the list which represents this list option.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var listElementID: Int { get }
```

#### Discussion

The set of elements in the list may change depending on other configuration parameters, so while the index of an element in this list may change, this ID never changes and is used to report list element selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingparameter/listelement/listelementid)*