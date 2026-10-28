# PHAssetResourceDataRequestID

**Framework**: Photos  
**Kind**: typealias  
**Role**: Type Alias

A numeric identifier for an asynchronous asset resource loading request.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
typealias PHAssetResourceDataRequestID = Int32
```

```c
typedef int32_t PHAssetResourceDataRequestID;
```

## Discussion

Pass this identifier to the [`cancelDataRequest(_:)`](./phassetresourcemanager/canceldatarequest%28_%29.md) method if you need to cancel a request before it completes.

## See Also

### Constants
- [Resource Loading Request Identifiers](../PhotoKit/resource-loading-request-identifiers.md)
  Special values for the [`PHAssetResourceDataRequestID`](./phassetresourcedatarequestid.md) identifier that are returned by asynchronous requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourcedatarequestid)*