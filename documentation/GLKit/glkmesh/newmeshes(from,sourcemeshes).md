# newMeshes(from:sourceMeshes:)

**Framework**: GLKit  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 9.0+ - Deprecated in 12.0
- iPadOS 9.0+ - Deprecated in 12.0
- macOS 10.11+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
class func newMeshes(from asset: MDLAsset, sourceMeshes: AutoreleasingUnsafeMutablePointer<NSArray?>?) throws -> [GLKMesh]
```

```objc
+ (NSArray<GLKMesh *> *) newMeshesFromAsset:(MDLAsset *) asset sourceMeshes:(NSArray<MDLMesh *> **) sourceMeshes error:(NSError **) error;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkmesh/newmeshes(from:sourcemeshes:))*