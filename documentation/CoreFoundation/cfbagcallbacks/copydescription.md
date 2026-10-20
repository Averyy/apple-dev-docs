# copyDescription

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Instance Property

The callback used to create a descriptive string representation of each value in the collection. If `NULL`, the collection will create a simple description of each value. See [`CFBagCopyDescriptionCallBack`](../cfbagcopydescriptioncallback.md) for a description of this callback.

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
var copyDescription: CFBagCopyDescriptionCallBack!
```

```c
CFBagCopyDescriptionCallBack copyDescription;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbagcallbacks/copydescription)*