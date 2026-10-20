# enabled

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether fog is applied to the fragment color.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var enabled: GLboolean { get set }
```

```objc
@property (nonatomic, assign) GLboolean enabled;
```

#### Discussion

If the value of this property is `GL_TRUE`, then fog calculations are performed each time a fragment is computed. If the value of this property is `GL_FALSE`, then fog calculations are skipped. The default value is `GL_TRUE`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectpropertyfog/enabled)*