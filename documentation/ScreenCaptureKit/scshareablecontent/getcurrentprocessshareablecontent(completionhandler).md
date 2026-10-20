# getCurrentProcessShareableContent(completionHandler:)

**Framework**: ScreenCaptureKit  
**Kind**: method  
**Role**: Type Method

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.4+

## Declaration

```swift
class func getCurrentProcessShareableContent(completionHandler: @escaping @Sendable (SCShareableContent?, (any Error)?) -> Void)
```

```swift
class var currentProcess: SCShareableContent { get async throws }
```

```objc
+ (void) getCurrentProcessShareableContentWithCompletionHandler:(void (^)(SCShareableContent *shareableContent, NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scshareablecontent/getcurrentprocessshareablecontent(completionhandler:))*