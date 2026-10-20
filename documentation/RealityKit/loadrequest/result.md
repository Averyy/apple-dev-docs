# result

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The result of the load operation.

**Availability**:
- iOS 13.0+ - Deprecated in 18.0
- iPadOS 13.0+ - Deprecated in 18.0
- Mac Catalyst 13.0+ - Deprecated in 18.0
- macOS 10.15+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
var result: Result<Output, any Error>? { get }
```

#### Discussion

A load operation can have the following results:

- `success(Output)` … The load operation has completed successfully.
- `failure(Error)` … The load operation failed.
- `nil` … The load operation is still in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/loadrequest/result)*