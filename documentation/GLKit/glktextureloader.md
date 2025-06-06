# GLKTextureLoader

**Framework**: GLKit  
**Kind**: class

A utility class that simplifies loading OpenGL or OpenGL ES texture datas from a variety of image file formats.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
class GLKTextureLoader
```

#### Overview

The [`GLKTextureLoader`](glktextureloader.md) class can load two-dimensional or cubemap textures in most image formats supported by the Image I/O framework. In iOS, it can also load textures compressed in the PVRTC format. It can load the data synchronously or asynchronously.

To load textures synchronously, make a context with the desired sharegroup the current context, and then call one or more of the class methods. The returned texture info object includes details about the loaded texture.

To load textures asynchronously, your initialization code allocates and initializes a new [`GLKTextureLoader`](glktextureloader.md) object using the sharegroup object that should be the destination for new textures. Then, to load a texture, your app calls one of the texture loader’s instance methods, passing in a completion handler block to be called when the texture has been loaded.

The following OpenGL properties are set for a newly created, non-mipmapped texture:

- `GL_TEXTURE_MIN_FILTER`:`GL_LINEAR`
- `GL_TEXTURE_MAG_FILTER`:`GL_LINEAR`
- `GL_TEXTURE_WRAP_S`:`GL_CLAMP_TO_EDGE`
- `GL_TEXTURE_WRAP_T`:`GL_CLAMP_TO_EDGE`

The following OpenGL properties are set for a newly created, mipmapped texture:

- `GL_TEXTURE_MIN_FILTER`:`GL_LINEAR_MIPMAP_LINEAR`
- `GL_TEXTURE_MAG_FILTER`:`GL_LINEAR`
- `GL_TEXTURE_WRAP_S`:`GL_CLAMP_TO_EDGE`
- `GL_TEXTURE_WRAP_T`:`GL_CLAMP_TO_EDGE`

The `GLKTextureLoader` and `GLKTextureInfo` classes do not manage the OpenGL texture for you. Once the texture is returned to your app, you are responsible for it. This means that after your app is finished using an OpenGL texture, it must explicitly deallocate it by calling the `glDeleteTextures` function.

## Topics

### Initialization
- [init(sharegroup: EAGLSharegroup)](glktextureloader/init(sharegroup:).md)
  Initializes a new texture loader object.
- [init(share: NSOpenGLContext)](glktextureloader/init(share:).md)
  Initializes a new texture loader object.
### Loading Textures from Files
- [class func texture(withContentsOfFile: String, options: [String : NSNumber]?) throws -> GLKTextureInfo](glktextureloader/texture(withcontentsoffile:options:).md)
  Loads a 2D texture image from a file and creates a new texture from the data.
- [func texture(withContentsOfFile: String, options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: GLKTextureLoaderCallback)](glktextureloader/texture(withcontentsoffile:options:queue:completionhandler:).md)
  Asynchronously loads a 2D texture image from a file and creates a new texture from the data.
### Loading a Texture From a URL
- [class func texture(withContentsOf: URL, options: [String : NSNumber]?) throws -> GLKTextureInfo](glktextureloader/texture(withcontentsof:options:)-708ft.md)
  Loads a 2D texture image from a URL and creates a new texture from the data.
- [func texture(withContentsOf: URL, options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: GLKTextureLoaderCallback)](glktextureloader/texture(withcontentsof:options:queue:completionhandler:)-55187.md)
  Asynchronously loads a 2D texture image from a URL and creates a new texture from the data.
### Creating Textures from In-Memory Representations
- [class func texture(withContentsOf: Data, options: [String : NSNumber]?) throws -> GLKTextureInfo](glktextureloader/texture(withcontentsof:options:)-2ljxb.md)
  Loads a 2D texture image from a memory range and creates a new texture from the data.
- [func texture(withContentsOf: Data, options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: GLKTextureLoaderCallback)](glktextureloader/texture(withcontentsof:options:queue:completionhandler:)-6n0cf.md)
  Asynchronously loads a 2D texture image from a memory range and creates a new texture from the data.
### Creating Textures from CGImages
- [class func texture(with: CGImage, options: [String : NSNumber]?) throws -> GLKTextureInfo](glktextureloader/texture(with:options:).md)
  Loads a 2D texture image from a Quartz image and creates a new texture from the data.
- [func texture(with: CGImage, options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: GLKTextureLoaderCallback)](glktextureloader/texture(with:options:queue:completionhandler:).md)
  Asynchronously loads a 2D texture image from a Quartz image and creates a new texture from the data.
### Loading Cube Maps from Files
- [class func cubeMap(withContentsOfFile: String, options: [String : NSNumber]?) throws -> GLKTextureInfo](glktextureloader/cubemap(withcontentsoffile:options:).md)
  Loads a cube map texture image from a single file and creates a new texture from the data.
- [func cubeMap(withContentsOfFile: String, options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: GLKTextureLoaderCallback)](glktextureloader/cubemap(withcontentsoffile:options:queue:completionhandler:).md)
  Asynchronously loads a cube map texture image from a single file and creates a new texture from the data.
- [class func cubeMap(withContentsOfFiles: [Any], options: [String : NSNumber]?) throws -> GLKTextureInfo](glktextureloader/cubemap(withcontentsoffiles:options:).md)
  Loads a cube map texture image from a series of files and creates a new texture from the data.
- [func cubeMap(withContentsOfFiles: [Any], options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: GLKTextureLoaderCallback)](glktextureloader/cubemap(withcontentsoffiles:options:queue:completionhandler:).md)
  Asynchronously loads a cube map texture image from a series of files and creates a new texture from the data.
### Loading Cube Maps from URLs
- [class func cubeMap(withContentsOf: URL, options: [String : NSNumber]?) throws -> GLKTextureInfo](glktextureloader/cubemap(withcontentsof:options:).md)
  Loads a cube map texture image from a single URL and creates a new texture from the data.
- [func cubeMap(withContentsOf: URL, options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: GLKTextureLoaderCallback)](glktextureloader/cubemap(withcontentsof:options:queue:completionhandler:).md)
  Asynchronously loads a cube map texture image from a single URL and creates a new texture from the data.
### Constants
- [typealias GLKTextureLoaderCallback](glktextureloadercallback.md)
  Signature for the block executed after an asynchronous texture loading operation completes.
- [Texture Loading Options](texture-loading-options.md)
  Keys to specify in a `textureOperations` dictionary.
- [Texture Error Handling](texture-error-handling.md)
  Strings used when handling error messages returned from a texture loading method.
- [GLKTextureLoaderError.Code](glktextureloadererror-swift.struct/code.md)
  Values to be returned when a texture loader encounters an error.
### Instance Methods
- [func texture(withName: String, scaleFactor: CGFloat, bundle: Bundle?, options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: GLKTextureLoaderCallback)](glktextureloader/texture(withname:scalefactor:bundle:options:queue:completionhandler:).md)
### Type Methods
- [class func texture(withName: String, scaleFactor: CGFloat, bundle: Bundle?, options: [String : NSNumber]?) throws -> GLKTextureInfo](glktextureloader/texture(withname:scalefactor:bundle:options:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class GLKTextureInfo](glktextureinfo.md)
  Information about OpenGL textures created by the [`GLKTextureLoader`](glktextureloader.md) class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureloader)*