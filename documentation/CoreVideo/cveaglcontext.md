# CVEAGLContext

**Framework**: Core Video  
**Kind**: typealias  
**Role**: Type Alias

A type that resolves to an [`EAGLContext`](../OpenGLES/eaglcontext.md) pointer when appropriate.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS*

```swift
typealias CVEAGLContext = EAGLContext
```

*visionOS*

```swift
typealias CVEAGLContext = UnsafeMutableRawPointer
```

*iOS, iPadOS, Mac Catalyst, tvOS*

```c
typedef EAGLContext * CVEAGLContext;
```

*visionOS*

```c
typedef void * CVEAGLContext;
```

#### Discussion

Core Video can be included in procedural C projects as well as Objective-C projects, so this type resolves to `void *` when using the former.

## See Also

### Data Types
- [class CVOpenGLESTextureCache](./cvopenglestexturecache.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cveaglcontext)*