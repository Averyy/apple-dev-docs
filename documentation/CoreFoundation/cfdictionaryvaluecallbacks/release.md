# release

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Instance Property

The callback used to release values as they are removed from the dictionary. If `NULL`, values are not released. See [`CFDictionaryReleaseCallBack`](../cfdictionaryreleasecallback.md) for a description of this callback.

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
var release: CFDictionaryReleaseCallBack!
```

```c
CFDictionaryReleaseCallBack release;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionaryvaluecallbacks/release)*