---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/synchronize(completion:)"
framework: "CareKit/CareKitStore"
---

# synchronize(completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Synchronizes the on device store with one on a remote server.

## Declaration

```swift
func synchronize(completion: @escaping @Sendable (Error?) -> Void)
```

## Discussion

Depending on the mode, it possible to overwrite the entire contents of the device or the remote with the data from the other.

> **See Also**: OCKRemoteSynchronizable

## Parameters

- `completion`: A completion closure that will be called when syncing completes.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/synchronize(completion:))*