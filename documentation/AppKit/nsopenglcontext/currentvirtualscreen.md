# currentVirtualScreen

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns the current virtual screen for the OpenGL context.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Please use Metal or MetalKit.

## Declaration

```swift
var currentVirtualScreen: GLint { get set }
```

```objc
@property GLint currentVirtualScreen;
```

## Return Value

The virtual screen number, which is a value between 0 and the number of virtual screens minus one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/currentvirtualscreen)*