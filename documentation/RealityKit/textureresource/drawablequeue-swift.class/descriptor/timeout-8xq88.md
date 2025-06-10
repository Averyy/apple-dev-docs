# timeout

**Framework**: RealityKit  
**Kind**: property

Specifies a timeout value in seconds when querying nextDrawable(). nextDrawable() will be blocked for up to the specified timeout period for a drawable to become available else throws `NextDrawableError.timeoutReached`. By default this is set to 1 second. Note that if `allowsNextDrawableTimeout` is false, then the timeout parameter will be ignored.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
var timeout: Duration { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/drawablequeue-swift.class/descriptor/timeout-8xq88)*