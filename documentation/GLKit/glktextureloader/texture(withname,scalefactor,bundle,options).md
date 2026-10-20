# texture(withName:scaleFactor:bundle:options:)

**Framework**: GLKit  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
class func texture(withName name: String, scaleFactor: CGFloat, bundle: Bundle?, options: [String : NSNumber]? = nil) throws -> GLKTextureInfo
```

```objc
+ (GLKTextureInfo *) textureWithName:(NSString *) name scaleFactor:(CGFloat) scaleFactor bundle:(NSBundle *) bundle options:(NSDictionary<NSString *,NSNumber *> *) options error:(NSError **) outError;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureloader/texture(withname:scalefactor:bundle:options:))*