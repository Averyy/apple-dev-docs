# collect(queue:completion:)

**Framework**: Network  
**Kind**: method

Stops an outstanding data transfer report and delivers the result.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@preconcurrency
func collect(queue: DispatchQueue, completion: @escaping (NWConnection.DataTransferReport) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/pendingdatatransferreport/collect(queue:completion:))*