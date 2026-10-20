# readAttributePaths(_:eventPaths:params:queue:completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func readAttributePaths(_ attributePaths: [MTRAttributeRequestPath]?, eventPaths: [MTREventRequestPath]?, params: MTRReadParams?, queue: dispatch_queue_t, completion: @escaping @Sendable ([[String : Any]]?, (any Error)?) -> Void)
```

```swift
func readAttributePaths(_ attributePaths: [MTRAttributeRequestPath]?, eventPaths: [MTREventRequestPath]?, params: MTRReadParams?, queue: dispatch_queue_t) async throws -> [[String : Any]]
```

```objc
- (void) readAttributePaths:(NSArray<MTRAttributeRequestPath *> *) attributePaths eventPaths:(NSArray<MTREventRequestPath *> *) eventPaths params:(MTRReadParams *) params queue:(dispatch_queue_t) queue completion:(MTRDeviceResponseHandler) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbasedevice/readattributepaths(_:eventpaths:params:queue:completion:))*