# GLKit

**Framework**: GLKit  
**Kind**: module

Speed up OpenGL ES or OpenGL app development. Use math libraries, background texture loading, pre-created shader effects, and a standard view and view controller to implement your rendering loop.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

#### Overview

The GLKit framework provides functions and classes that reduce the effort required to create new shader-based apps or to port existing apps that rely on fixed-function vertex or fragment processing provided by earlier versions of OpenGL ES or OpenGL.

##### Glkit Features

GLKit provides functionality in four key areas:

-  allows your app to easily load textures from a variety of sources. Textures can even be loaded asynchronously in the background with just a few lines of code. For more information, see [`GLKTextureLoader`](glktextureloader.md).
-  provide commonly used vector, quaternion and matrix operations. These implementations are optimized to provide great performance.
-  provide standard implementations of common shader effects. You configure the effect and the associated vertex data; the effect creates and loads an appropriate shader. GLKit includes three effects: The [`GLKBaseEffect`](glkbaseeffect.md) class implements a critical subset of the OpenGL ES 1.1 shading and lighting model, the [`GLKReflectionMapEffect`](glkreflectionmapeffect.md) class extends the base effect to include reflection mapping support, and the [`GLKSkyboxEffect`](glkskyboxeffect.md) class provides an implementation of a skybox effect.
-  provide a standard implementation of an OpenGL ES view and a corresponding view controller. This reduces the amount of code needed to create an iOS app that use OpenGL ES. For more information, see [`GLKView`](glkview.md) and [`GLKViewController`](glkviewcontroller.md).

On iOS, GLKit requires an OpenGL ES 2.0 context. In macOS, GLKit requires an OpenGL context that supports the OpenGL 3.2 Core Profile.

## Topics

### Texture Loading
- [class GLKTextureInfo](glktextureinfo.md)
  Information about OpenGL textures created by the [`GLKTextureLoader`](glktextureloader.md) class.
- [class GLKTextureLoader](glktextureloader.md)
  A utility class that simplifies loading OpenGL or OpenGL ES texture datas from a variety of image file formats.
### OpenGL ES View Rendering
- [class GLKView](glkview.md)
  A default implementation for views that draw their content using OpenGL ES.
- [protocol GLKViewDelegate](glkviewdelegate.md)
  Drawing callback methods for use with a [`GLKView`](glkview.md) object.
- [class GLKViewController](glkviewcontroller.md)
  A view controller that manages an OpenGL ES rendering loop.
- [protocol GLKViewControllerDelegate](glkviewcontrollerdelegate.md)
  Rendering loop callback methods for use with a [`GLKViewController`](glkviewcontroller.md) object.
### Mesh Data Management
- [class GLKMesh](glkmesh.md)
- [class GLKMeshBuffer](glkmeshbuffer.md)
- [class GLKMeshBufferAllocator](glkmeshbufferallocator.md)
- [class GLKSubmesh](glksubmesh.md)
### Shader-Based Rendering Effects
- [protocol GLKNamedEffect](glknamedeffect.md)
  A standard interface for objects that provide shader-based OpenGL rendering effects.
- [class GLKBaseEffect](glkbaseeffect.md)
  A simple lighting and shading system for use in shader-based OpenGL rendering.
- [class GLKReflectionMapEffect](glkreflectionmapeffect.md)
  A lighting and shading system that supports reflection mapping for use in shader-based OpenGL rendering.
- [class GLKSkyboxEffect](glkskyboxeffect.md)
  A simple skybox visual effect for use in shader-based OpenGL rendering.
### Rendering Effect Parameters
- [class GLKEffectProperty](glkeffectproperty.md)
  The abstract superclass for configuration information used in GLKit rendering effects.
- [class GLKEffectPropertyFog](glkeffectpropertyfog.md)
  Fog drawing information for use in GLKit rendering effects.
- [class GLKEffectPropertyLight](glkeffectpropertylight.md)
  Lighting information for use in GLKit rendering effects.
- [class GLKEffectPropertyTexture](glkeffectpropertytexture.md)
  Texture drawing parameters for use in GLKit rendering effects.
- [class GLKEffectPropertyMaterial](glkeffectpropertymaterial.md)
  Surface appearance properties for use in GLKit rendering effects.
- [class GLKEffectPropertyTransform](glkeffectpropertytransform.md)
  Coordinate transform information for use in GLKit rendering effects.
- [GLKit Effects Constants](glkit-effects-constants.md)
### Math Utilties
- [class GLKMatrixStack](glkmatrixstack.md)
  An opaque type that represents a stack of 4 x 4 matrices, providing support for hierarchical transform modeling and similar tasks.
- [GLKMatrix3](glkmatrix3-pcl.md)
- [GLKMatrix4](glkmatrix4-pce.md)
- [GLKVector2](glkvector2-pbj.md)
- [GLKVector3](glkvector3-pbt.md)
- [GLKVector4](glkvector4-pbk.md)
- [GLKQuaternion](glkquaternion-pc6.md)
- [GLKit Math Utilities](glkit-math-utilities.md)
### Reference
- [GLKit Structures](glkit-structures.md)
- [GLKit Enumerations](glkit-enumerations.md)
- [GLKit Constants](glkit-constants.md)
- [GLKit Functions](glkit-functions.md)
- [GLKit Data Types](glkit-data-types.md)

## See Also

- [OpenGL Programming Guide for Mac](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGL-MacProgGuide/opengl_intro/opengl_intro.html#//apple_ref/doc/uid/TP40001987)
- [OpenGL ES Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/3DDrawing/Conceptual/OpenGLES_ProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008793)


---

*[View on Apple Developer](https://developer.apple.com/documentation/GLKit)*