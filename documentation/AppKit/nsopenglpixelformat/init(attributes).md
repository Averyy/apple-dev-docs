# init(attributes:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Returns an OpenGL pixel format object initialized with specified pixel format attributes.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Please use Metal or MetalKit.

## Declaration

```swift
convenience init?(attributes attribs: UnsafePointer<NSOpenGLPixelFormatAttribute>)
```

```objc
- (instancetype) initWithAttributes:(const NSOpenGLPixelFormatAttribute *) attribs;
```

## Return Value

An initialized `NSOpenGLPixelFormat` object whose attributes match the desired attributes as close as possible, or `nil` if an object with the desired attributes could not be initialized.

## Discussion

On return, the Boolean attributes of the receiver match the values specified in `attribs`, and the integer attributes are as close to the specified values as can be provided by the system.

The existence of a Boolean attribute constant in `attribs` implies a [`true`](../../Swift/true.md) value. The Boolean attribute constants are:

- `NSOpenGLPFAAllRenderers`
- `NSOpenGLPFADoubleBuffer`
- `NSOpenGLPFAStereo`
- `NSOpenGLPFAMinimumPolicy`
- `NSOpenGLPFAMaximumPolicy`
- `NSOpenGLPFAOffScreen`
- `NSOpenGLPFAFullScreen`
- `NSOpenGLPFASingleRenderer`
- `NSOpenGLPFANoRecovery`
- `NSOpenGLPFAAccelerated`
- `NSOpenGLPFAClosestPolicy`
- `NSOpenGLPFARobust`
- `NSOpenGLPFABackingStore`
- `NSOpenGLPFAWindow`
- `NSOpenGLPFAMultiScreen`
- `NSOpenGLPFACompliant`
- `NSOpenGLPFAPixelBuffer`

The integer constants must be followed by a value. These constants are:

- `NSOpenGLPFAAuxBuffers`
- `NSOpenGLPFAColorSize`
- `NSOpenGLPFAAlphaSize`
- `NSOpenGLPFADepthSize`
- `NSOpenGLPFAStencilSize`
- `NSOpenGLPFAAccumSize`
- `NSOpenGLPFARendererID`
- `NSOpenGLPFAScreenMask`

This code fragment creates a double-buffered pixel format with a 32-bit depth buffer:

```objc
NSOpenGLPixelFormatAttribute attrs[] =
{
    NSOpenGLPFADoubleBuffer,
    NSOpenGLPFADepthSize, 32,
    0
};
 
NSOpenGLPixelFormat* pixFmt = [[NSOpenGLPixelFormat alloc] initWithAttributes:attrs];
 
/* Check if initWithAttributes succeeded. */
if(pixFmt == nil) {
    /* initWithAttributes failed. Try to alloc/init with a different  list of attributes. */
}
```

## Parameters

- `attribs`: A 0-terminated array containing Boolean and integer attribute constants. The presence of a Boolean attribute implies a value of [`true`](../../Swift/true.md) while its absence implies a value of [`false`](../../Swift/false.md). Integer constants must be followed by the desired value. For a listing of attribute constants, see the constants in [OpenGL Pixel Format Attributes](../opengl-pixel-format-attributes.md).

## See Also

### Related Documentation
- [func getValues(UnsafeMutablePointer<GLint>, forAttribute: NSOpenGLPixelFormatAttribute, forVirtualScreen: GLint)](./getvalues%28_,forattribute,forvirtualscreen%29.md)
  Gets the value for the specified pixel format attribute.
### Creating an OpenGL Pixel Format
- [init?(cglPixelFormatObj: CGLPixelFormatObj)](./init%28cglpixelformatobj%29-2zqw4.md)
  Returns an OpenGL pixel format object initialized with using an existing CGL pixel format object.
- [- initWithData:](./initwithdata_.md)
  Returns an OpenGL pixel format object initialized with specified pixel format attribute data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglpixelformat/init(attributes:))*