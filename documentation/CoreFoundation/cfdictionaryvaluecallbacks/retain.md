# retain

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Instance Property

The callback used to retain each value as they are added to the collection. This callback returns the value to use as the value in the dictionary, which is usually the value parameter passed to this callback, but may be a different value if a different value should be used as the value. If `NULL`, values are not retained. See [`CFDictionaryRetainCallBack`](../cfdictionaryretaincallback.md) for a descriptions of this function’s parameters.

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
var retain: CFDictionaryRetainCallBack!
```

```c
CFDictionaryRetainCallBack retain;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionaryvaluecallbacks/retain)*