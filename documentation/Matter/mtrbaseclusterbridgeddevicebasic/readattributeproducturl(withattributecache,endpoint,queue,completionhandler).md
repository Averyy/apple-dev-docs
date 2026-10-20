# readAttributeProductURL(withAttributeCache:endpoint:queue:completionHandler:)

**Framework**: Matter  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- tvOS 16.1+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.4

> **Deprecated**: Please use readAttributeProductURLWithAttributeCache:endpoint:queue:completion:

## Declaration

```swift
class func readAttributeProductURL(withAttributeCache attributeCacheContainer: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t, completionHandler: @escaping @Sendable (String?, (any Error)?) -> Void)
```

```swift
class func readAttributeProductURL(withAttributeCache attributeCacheContainer: MTRAttributeCacheContainer, endpoint: NSNumber, queue: dispatch_queue_t) async throws -> String
```

```objc
+ (void) readAttributeProductURLWithAttributeCache:(MTRAttributeCacheContainer *) attributeCacheContainer endpoint:(NSNumber *) endpoint queue:(dispatch_queue_t) queue completionHandler:(void (^)(NSString *value, NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterbridgeddevicebasic/readattributeproducturl(withattributecache:endpoint:queue:completionhandler:))*