# GLKTextureLoader

**Framework**: GLKit  
**Kind**: class  
**Role**: Class

A utility class that simplifies loading OpenGL or OpenGL ES texture datas from a variety of image file formats.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
class GLKTextureLoader
```

```objc
@interface GLKTextureLoader : NSObject
```

#### Overview

The [`GLKTextureLoader`](./glktextureloader.md) class can load two-dimensional or cubemap textures in most image formats supported by the Image I/O framework. In iOS, it can also load textures compressed in the PVRTC format. It can load the data synchronously or asynchronously.

To load textures synchronously, make a context with the desired sharegroup the current context, and then call one or more of the class methods. The returned texture info object includes details about the loaded texture.

To load textures asynchronously, your initialization code allocates and initializes a new [`GLKTextureLoader`](./glktextureloader.md) object using the sharegroup object that should be the destination for new textures. Then, to load a texture, your app calls one of the texture loader’s instance methods, passing in a completion handler block to be called when the texture has been loaded.

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
- [init(sharegroup: EAGLSharegroup)](./glktextureloader/init%28sharegroup%29.md)
  Initializes a new texture loader object.
- [init(share: NSOpenGLContext)](./glktextureloader/init%28share%29.md)
  Initializes a new texture loader object.
### Loading Textures from Files
- [class func texture(withContentsOfFile: String, options: [String : NSNumber]?) throws -> GLKTextureInfo](./glktextureloader/texture%28withcontentsoffile,options%29.md)
  Loads a 2D texture image from a file and creates a new texture from the data.
- [func texture(withContentsOfFile: String, options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: (GLKTextureInfo?, (any Error)?) -> Void)](./glktextureloader/texture%28withcontentsoffile,options,queue,completionhandler%29.md)
  Asynchronously loads a 2D texture image from a file and creates a new texture from the data.
### Loading a Texture From a URL
- [class func texture(withContentsOf: URL, options: [String : NSNumber]?) throws -> GLKTextureInfo](./glktextureloader/texture%28withcontentsof,options%29-708ft.md)
  Loads a 2D texture image from a URL and creates a new texture from the data.
- [func texture(withContentsOf: URL, options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: (GLKTextureInfo?, (any Error)?) -> Void)](./glktextureloader/texture%28withcontentsof,options,queue,completionhandler%29-55187.md)
  Asynchronously loads a 2D texture image from a URL and creates a new texture from the data.
### Creating Textures from In-Memory Representations
- [class func texture(withContentsOf: Data, options: [String : NSNumber]?) throws -> GLKTextureInfo](./glktextureloader/texture%28withcontentsof,options%29-2ljxb.md)
  Loads a 2D texture image from a memory range and creates a new texture from the data.
- [func texture(withContentsOf: Data, options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: (GLKTextureInfo?, (any Error)?) -> Void)](./glktextureloader/texture%28withcontentsof,options,queue,completionhandler%29-6n0cf.md)
  Asynchronously loads a 2D texture image from a memory range and creates a new texture from the data.
### Creating Textures from CGImages
- [class func texture(with: CGImage, options: [String : NSNumber]?) throws -> GLKTextureInfo](./glktextureloader/texture%28with,options%29.md)
  Loads a 2D texture image from a Quartz image and creates a new texture from the data.
- [func texture(with: CGImage, options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: (GLKTextureInfo?, (any Error)?) -> Void)](./glktextureloader/texture%28with,options,queue,completionhandler%29.md)
  Asynchronously loads a 2D texture image from a Quartz image and creates a new texture from the data.
### Loading Cube Maps from Files
- [class func cubeMap(withContentsOfFile: String, options: [String : NSNumber]?) throws -> GLKTextureInfo](./glktextureloader/cubemap%28withcontentsoffile,options%29.md)
  Loads a cube map texture image from a single file and creates a new texture from the data.
- [func cubeMap(withContentsOfFile: String, options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: (GLKTextureInfo?, (any Error)?) -> Void)](./glktextureloader/cubemap%28withcontentsoffile,options,queue,completionhandler%29.md)
  Asynchronously loads a cube map texture image from a single file and creates a new texture from the data.
- [class func cubeMap(withContentsOfFiles: [Any], options: [String : NSNumber]?) throws -> GLKTextureInfo](./glktextureloader/cubemap%28withcontentsoffiles,options%29.md)
  Loads a cube map texture image from a series of files and creates a new texture from the data.
- [func cubeMap(withContentsOfFiles: [Any], options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: (GLKTextureInfo?, (any Error)?) -> Void)](./glktextureloader/cubemap%28withcontentsoffiles,options,queue,completionhandler%29.md)
  Asynchronously loads a cube map texture image from a series of files and creates a new texture from the data.
### Loading Cube Maps from URLs
- [class func cubeMap(withContentsOf: URL, options: [String : NSNumber]?) throws -> GLKTextureInfo](./glktextureloader/cubemap%28withcontentsof,options%29.md)
  Loads a cube map texture image from a single URL and creates a new texture from the data.
- [func cubeMap(withContentsOf: URL, options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: (GLKTextureInfo?, (any Error)?) -> Void)](./glktextureloader/cubemap%28withcontentsof,options,queue,completionhandler%29.md)
  Asynchronously loads a cube map texture image from a single URL and creates a new texture from the data.
### Constants
- [typealias GLKTextureLoaderCallback](./glktextureloadercallback.md)
  Signature for the block executed after an asynchronous texture loading operation completes.
- [Texture Loading Options](./texture-loading-options.md)
  Keys to specify in a `textureOperations` dictionary.
- [Texture Error Handling](./texture-error-handling.md)
  Strings used when handling error messages returned from a texture loading method.
- [GLKTextureLoaderError.Code](./glktextureloadererror-swift.struct/code.md)
  Values to be returned when a texture loader encounters an error.
### Instance Methods
- [func texture(withName: String, scaleFactor: CGFloat, bundle: Bundle?, options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: (GLKTextureInfo?, (any Error)?) -> Void)](./glktextureloader/texture%28withname,scalefactor,bundle,options,queue,completionhandler%29.md)
### Type Methods
- [class func texture(withName: String, scaleFactor: CGFloat, bundle: Bundle?, options: [String : NSNumber]?) throws -> GLKTextureInfo](./glktextureloader/texture%28withname,scalefactor,bundle,options%29.md)
### Initializers
- [init(shareContext: NSOpenGLContext)](./glktextureloader/init%28sharecontext%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Texture Loading
- [class GLKTextureInfo](./glktextureinfo.md)
  Information about OpenGL textures created by the [`GLKTextureLoader`](./glktextureloader.md) class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureloader)*