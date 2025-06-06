# synchronizeToBackingStore(_:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Synchronizes changes to the backing store.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func synchronizeToBackingStore() async throws
```

#### Discussion

If `completionHandler` is `nil`, performs the operation synchronously. The `completionHandler` gets passed `error` if the synchronization fails. It should block (or fails if synchronous) when there’s an active transaction.

## Parameters

- `completionHandler`: A completion handler to run upon successful completion, or to process an error upon failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextelementprovider/synchronizetobackingstore(_:))*