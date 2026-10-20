# texture(withName:scaleFactor:bundle:options:queue:completionHandler:)

**Framework**: GLKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func texture(withName name: String, scaleFactor: CGFloat, bundle: Bundle?, options: [String : NSNumber]? = nil, queue: dispatch_queue_t?, completionHandler block: @escaping @Sendable (GLKTextureInfo?, (any Error)?) -> Void)
```

```swift
func texture(withName name: String, scaleFactor: CGFloat, bundle: Bundle?, options: [String : NSNumber]? = nil, queue: dispatch_queue_t?) async throws -> GLKTextureInfo
```

```objc
- (void) textureWithName:(NSString *) name scaleFactor:(CGFloat) scaleFactor bundle:(NSBundle *) bundle options:(NSDictionary<NSString *,NSNumber *> *) options queue:(dispatch_queue_t) queue completionHandler:(GLKTextureLoaderCallback) block;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureloader/texture(withname:scalefactor:bundle:options:queue:completionhandler:))*