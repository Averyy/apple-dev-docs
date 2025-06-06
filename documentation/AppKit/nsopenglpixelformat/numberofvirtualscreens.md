# numberOfVirtualScreens

**Framework**: AppKit  
**Kind**: property

The number of virtual screens associated with the OpenGL pixel format.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var numberOfVirtualScreens: GLint { get }
```

#### Return Value

The number of virtual screens.

#### Discussion

When the attributes are set, OpenGL searches for drivers matching the requested attributes. Each matching driver drives a set of displays. For example, a graphics card in a portable computer might drive the internal screen and an external display. This portable computer would have one virtual screen. A desktop computer might have two different graphics cards, each driving one or more displays. The pairing of an OpenGL driver with its set of associated displays corresponds to one virtual screen. In the above examples, the portable computer would have one virtual screen, while the desktop computer would have two. Another desktop computer with a video card driving two displays at once would have one virtual screen.

For more information on virtual screens, consult [`OpenGL Programming Guide for Mac`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGL-MacProgGuide/opengl_intro/opengl_intro.html#//apple_ref/doc/uid/TP40001987).

## See Also

- [var cglPixelFormatObj: CGLPixelFormatObj?](nsopenglpixelformat/cglpixelformatobj.md)
  The low-level, platform-specific Core OpenGL (CGL) pixel format object represented by the receiver.
- [func getValues(UnsafeMutablePointer<GLint>, forAttribute: NSOpenGLPixelFormatAttribute, forVirtualScreen: GLint)](nsopenglpixelformat/getvalues(_:forattribute:forvirtualscreen:).md)
  Gets the value for the specified pixel format attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglpixelformat/numberofvirtualscreens)*