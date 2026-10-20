# init(returnedOffset:)

**Framework**: FSKit  
**Kind**: init  
**Role**: Initializer

Creates a result for a region-seeking operation.

**Availability**:
- macOS 27.0+

## Declaration

```swift
init(returnedOffset: off_t)
```

```objc
- (instancetype) initWithReturnedOffset:(off_t) returnedOffset;
```

#### Return Value

A populated result instance, or `nil` if validation fails.

## Parameters

- `returnedOffset`: The offset of the requested region, greater than or equal to the supplied offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsseekregionresult/init(returnedoffset:))*