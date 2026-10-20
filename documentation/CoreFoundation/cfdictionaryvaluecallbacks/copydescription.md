# copyDescription

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Instance Property

The callback used to create a descriptive string representation of each value in the dictionary. If `NULL`, the collection will create a simple description of each value. See [`CFDictionaryCopyDescriptionCallBack`](../cfdictionarycopydescriptioncallback.md) for a description of this callback.

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
var copyDescription: CFDictionaryCopyDescriptionCallBack!
```

```c
CFDictionaryCopyDescriptionCallBack copyDescription;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionaryvaluecallbacks/copydescription)*