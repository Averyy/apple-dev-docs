# equal

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Instance Property

The callback used to compare values in the array for equality for some operations. If `NULL`, the collection will use pointer equality to compare values in the collection. See [`CFArrayEqualCallBack`](../cfarrayequalcallback.md) for a description of this callback.

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
var equal: CFArrayEqualCallBack!
```

```c
CFArrayEqualCallBack equal;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfarraycallbacks/equal)*