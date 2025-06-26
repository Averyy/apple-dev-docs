# CVEAGLContext

**Framework**: Core Video  
**Kind**: typealias

A type that resolves to an [`EAGLContext`](https://developer.apple.com/documentation/OpenGLES/EAGLContext) pointer when appropriate.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
typealias CVEAGLContext = EAGLContext
```

#### Discussion

Core Video can be included in procedural C projects as well as Objective-C projects, so this type resolves to `void *` when using the former.

## See Also

- [class CVOpenGLESTextureCache](cvopenglestexturecache.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cveaglcontext)*