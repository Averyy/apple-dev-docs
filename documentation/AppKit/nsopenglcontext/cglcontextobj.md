# cglContextObj

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns the low-level, platform-specific Core OpenGL (CGL) context object represented by the receiver.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Please use Metal or MetalKit.

## Declaration

```swift
var cglContextObj: CGLContextObj? { get }
```

```objc
@property (readonly, nullable) CGLContextObj CGLContextObj;
```

## Return Value

A pointer to the CGLContextObj data type represented by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/cglcontextobj)*