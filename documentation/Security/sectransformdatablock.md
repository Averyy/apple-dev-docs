# SecTransformDataBlock

**Framework**: Security  
**Kind**: typealias  
**Role**: Type Alias

A block used to override the default data handling for a transform.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias SecTransformDataBlock = (CFTypeRef) -> Unmanaged<CFTypeRef>?
```

```c
typedef const void *(^)(const void *) SecTransformDataBlock;
```

#### Return Value

`NULL` for the [`kSecTransformActionInternalizeExtraData`](./ksectransformactioninternalizeextradata.md) action, the data to be passed to the output attribute for any other action, or a [`CFError`](../CoreFoundation/cferror.md) instance on failure.

## Parameters

- `data`: The data to be processed. When this block is used to to implement the [`kSecTransformActionProcessData`](./ksectransformactionprocessdata.md) action, the data is the input data that is to be processed into the output data. When this block is used to implement the [`kSecTransformActionInternalizeExtraData`](./ksectransformactioninternalizeextradata.md) action, the data is a [`CFDictionary`](../CoreFoundation/cfdictionary.md) that contains the data that needs to be imported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformdatablock)*