# downloadAllResources(timeout:completionHandler:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- tvOS 27.2+
- visionOS 27.2+

## Declaration

```swift
class func downloadAllResources(timeout: TimeInterval, completionHandler: @escaping ((any Error)?) -> Void) -> Progress
```

```objc
+ (NSProgress *) downloadAllResourcesWithTimeout:(NSTimeInterval) timeout completionHandler:(void (^)(NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirawfilter/downloadallresources(timeout:completionhandler:))*