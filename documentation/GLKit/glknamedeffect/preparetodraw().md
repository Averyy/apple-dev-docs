# prepareToDraw()

**Framework**: GLKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Prepares an effect for OpenGL ES rendering.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
func prepareToDraw()
```

```objc
- (void) prepareToDraw;
```

## Discussion

An effect binds a compiled shader program to the context and returns. Many effects also bind data to other OpenGL state variables—see the appropriate reference for each effect class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glknamedeffect/preparetodraw())*