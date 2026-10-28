# synchronizeToBackingStore(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Synchronizes changes to the backing store.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func synchronizeToBackingStore(_ completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func synchronizeToBackingStore() async throws
```

```objc
- (void) synchronizeToBackingStore:(void (^)(NSError *error)) completionHandler;
```

## Discussion

If `completionHandler` is `nil`, performs the operation synchronously. The `completionHandler` gets passed `error` if the synchronization fails. It should block (or fails if synchronous) when there’s an active transaction.

## Parameters

- `completionHandler`: A completion handler to run upon successful completion, or to process an error upon failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextelementprovider/synchronizetobackingstore(_:))*