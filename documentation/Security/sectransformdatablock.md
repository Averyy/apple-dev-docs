# SecTransformDataBlock

**Framework**: Security  
**Kind**: typealias

A block used to override the default data handling for a transform.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias SecTransformDataBlock = (CFTypeRef) -> Unmanaged<CFTypeRef>?
```

#### Return Value

`NULL` for the [`kSecTransformActionInternalizeExtraData`](ksectransformactioninternalizeextradata.md) action, the data to be passed to the output attribute for any other action, or a doc://com.apple.documentation/documentation/corefoundation/cferror-ru8 instance on failure.

## Parameters

- `data`: The data to be processed. When this block is used to to implement the   action, the data is the input data that is to be processed into the output data. When this block is used to implement the   action, the data is a   that contains the data that needs to be imported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformdatablock)*