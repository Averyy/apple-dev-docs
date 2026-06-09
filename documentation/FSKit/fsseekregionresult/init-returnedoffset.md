# init(returnedOffset:)

**Framework**: FSKit  
**Kind**: init

Creates a result for a region-seeking operation.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
init(returnedOffset: off_t)
```

#### Return Value

A populated result instance, or `nil` if validation fails.

## Parameters

- `returnedOffset`: The offset of the requested region, greater than or equal to the supplied offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsseekregionresult/init(returnedoffset:))*