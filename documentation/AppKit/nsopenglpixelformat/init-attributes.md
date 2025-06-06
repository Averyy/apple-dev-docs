# init(attributes:)

**Framework**: AppKit  
**Kind**: init

Returns an OpenGL pixel format object initialized with specified pixel format attributes.

**Availability**:
- macOS 10.0+

## Declaration

```swift
convenience init?(attributes attribs: UnsafePointer<NSOpenGLPixelFormatAttribute>)
```

#### Return Value

An initialized `NSOpenGLPixelFormat` object whose attributes match the desired attributes as close as possible, or `nil` if an object with the desired attributes could not be initialized.

#### Discussion

On return, the Boolean attributes of the receiver match the values specified in `attribs`, and the integer attributes are as close to the specified values as can be provided by the system.

The existence of a Boolean attribute constant in `attribs` implies a [`true`](https://developer.apple.com/documentation/swift/true) value. The Boolean attribute constants are:

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

- `attribs`: A 0-terminated array containing Boolean and integer attribute constants. The presence of a Boolean attribute implies a value of   while its absence implies a value of  . Integer constants must be followed by the desired value. For a listing of attribute constants, see the constants in  .

## See Also

- [func getValues(UnsafeMutablePointer<GLint>, forAttribute: NSOpenGLPixelFormatAttribute, forVirtualScreen: GLint)](nsopenglpixelformat/getvalues(_:forattribute:forvirtualscreen:).md)
  Gets the value for the specified pixel format attribute.
- [init?(cglPixelFormatObj: CGLPixelFormatObj)](nsopenglpixelformat/init(cglpixelformatobj:).md)
  Returns an OpenGL pixel format object initialized with using an existing CGL pixel format object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglpixelformat/init(attributes:))*