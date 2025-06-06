# kEAGLDrawablePropertyRetainedBacking

**Framework**: OpenGL ES  
**Kind**: var

The key specifying whether the drawable surface retains its contents after displaying them.  The value for this key is an `NSNumber` object containing a `BOOL` data type. If `false`, you may not rely on the contents being the same after the contents are displayed.  If `true`, then the contents will not change after being displayed. Setting the value to `true` is recommended only when you need the content to remain unchanged, as using it can result in both reduced performance and additional memory usage. The default value is `false`.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 2.0+
- tvOS 9.0+

## Declaration

```swift
let kEAGLDrawablePropertyRetainedBacking: String
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/opengles/keagldrawablepropertyretainedbacking)*