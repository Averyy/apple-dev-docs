# Model I/O

**Framework**: Model I/O  
**Kind**: module

Import, export, and manipulate 3D models using a common infrastructure that integrates MetalKit, GLKit, and SceneKit.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

#### Overview

The Model I/O framework provides a system-level understanding of 3D model assets and related resources. You can use this framework to import and export assets from and to a variety of industry standard file formats supported by popular authoring tools and game engines. You can also use Model I/O to generate or process model and texture data—for example, to create subdivision surfaces, to bake ambient occlusion textures, or to generate light probes. Model I/O can share data buffers with the MetalKit, GLKit, and SceneKit frameworks to help you load, process, and render 3D assets efficiently.

##### Model Io Features

- Importing and exporting 3D assets. A [`MDLAsset`](mdlasset.md) object represents a collection of objects that describe elements of a 3D scene—[`MDLMesh`](mdlmesh.md), [`MDLLight`](mdllight.md), and [`MDLCamera`](mdlcamera.md) objects. Use the [`MDLAsset`](mdlasset.md) class to load these objects from a file or to create a collection of 3D objects for export to a file.
- Working with 3D model data. Use the [`MDLVertexDescriptor`](mdlvertexdescriptor.md) class to inspect or rearrange a mesh’s vertex and index data format. Use classes that adopt the [`MDLMeshBuffer`](mdlmeshbuffer.md) and [`MDLMeshBufferAllocator`](mdlmeshbufferallocator.md) protocols to minimize the number of times a mesh’s vertex and index data is copied and translated between loading, processing, and rendering on a GPU. The MetalKit and GLKit frameworks provide such classes—see [`MetalKit`](https://developer.apple.com/documentation/MetalKit) and [`GLKit`](https://developer.apple.com/documentation/GLKit).
- Processing and generating asset data. Use [`MDLMesh`](mdlmesh.md) methods (for example, the  [`addNormals(withAttributeNamed:creaseThreshold:)`](mdlmesh/addnormals(withattributenamed:creasethreshold:).md) method) to process a model, generating additional data—such as surface normals, tangent basis vectors, ambient occlusion, or light maps—for use in rendering. Use the [`MDLTexture`](mdltexture.md) class and its subclasses to generate procedural textures such as noise, normal maps, and realistic sky boxes. Use the [`MDLLightProbe`](mdllightprobe.md) class to generate light sources whose illumination is based on the contents of a scene. Use the [`MDLVoxelArray`](mdlvoxelarray.md) class to work with a volumetric description of a model.
- Describing realistic rendering parameters. The [`MDLPhysicallyPlausibleScatteringFunction`](mdlphysicallyplausiblescatteringfunction.md) class—one of many ways to describe the surface appearance for a [`MDLMaterial`](mdlmaterial.md) object associated with a mesh—defines the intended rendering of a surface using the same physically based shading systems seen in popular feature films and high-end game engines. The [`MDLPhotometricLight`](mdlphotometriclight.md) and [`MDLPhysicallyPlausibleLight`](mdlphysicallyplausiblelight.md) classes describe realistic lighting properties for use in rendering, and the [`MDLCamera`](mdlcamera.md) class also supports physically based rendering parameters.

## Topics

### 3D Asset Basics
- [class MDLAsset](mdlasset.md)
  An indexed container for 3D objects and associated information, such as transform hierarchies, meshes, cameras, and lights.
- [class MDLObject](mdlobject.md)
  The base class for objects that are part of a 3D asset, including meshes, cameras, and lights.
- [class MDLTransform](mdltransform.md)
  A description of the local coordinate space transformations for a 3D object.
- [class MDLMesh](mdlmesh.md)
  A container for vertex buffer data to be used in rendering a 3D object.
- [class MDLSubmesh](mdlsubmesh.md)
  A container for index buffer data and material information to be used in rendering all or part of a 3D object.
- [class MDLSubmeshTopology](mdlsubmeshtopology.md)
  A description of how a submesh’s index buffer data is arranged and how that arrangement should be used to produce the submesh’s intended 3D shape.
- [protocol MDLNamed](mdlnamed.md)
  The common interface for Model I/O objects that expose a human-readable name.
### Managing Mesh Data
- [protocol MDLMeshBuffer](mdlmeshbuffer.md)
  The general interface for managing storage of vertex and index data used in loading, processing, and rendering meshes.
- [protocol MDLMeshBufferAllocator](mdlmeshbufferallocator.md)
  The general interface for managing allocation of data buffers to be used in loading, processing, and rendering meshes.
- [class MDLMeshBufferData](mdlmeshbufferdata.md)
  A memory buffer that stores vertex or index data for a Model I/O mesh.
- [class MDLMeshBufferDataAllocator](mdlmeshbufferdataallocator.md)
  A basic allocator implementation that allocates from main memory using data objects.
- [class MDLMeshBufferMap](mdlmeshbuffermap.md)
  An object that manages access to a memory buffer used for the data storage of a Model I/O mesh.
- [protocol MDLMeshBufferZone](mdlmeshbufferzone.md)
  The general interface for logical pools of memory used in allocation of related mesh data buffers.
- [class MDLMeshBufferZoneDefault](mdlmeshbufferzonedefault.md)
  A standard implementation of the [`MDLMeshBufferZone`](mdlmeshbufferzone.md) protocol.
- [class MDLVertexAttribute](mdlvertexattribute.md)
  A description of the format of per-vertex data for a single vertex attribute in a mesh object.
- [class MDLVertexAttributeData](mdlvertexattributedata.md)
  An object that provides convenience access to vertex data for a specific vertex attribute of a mesh.
- [class MDLVertexBufferLayout](mdlvertexbufferlayout.md)
  A [`MDLVertexBufferLayout`](mdlvertexbufferlayout.md) object describes layout information for a vertex buffer in a [`MDLMesh`](mdlmesh.md) object. A collection of vertex layer objects, vertex attribute objects, and additional information forms a [`MDLVertexDescriptor`](mdlvertexdescriptor.md) object, which completely describes the layout of vertex buffers for a mesh.
- [class MDLVertexDescriptor](mdlvertexdescriptor.md)
  A description of the structure, format, and layout for vertex data buffers associated with a mesh.
### Materials
- [class MDLMaterial](mdlmaterial.md)
  A collection of material properties that together describe the intended surface appearance for rendering a 3D object.
- [class MDLMaterialProperty](mdlmaterialproperty.md)
  A definition for one specific aspect of the rendering parameters for a material.
- [class MDLMaterialPropertyConnection](mdlmaterialpropertyconnection.md)
- [class MDLMaterialPropertyGraph](mdlmaterialpropertygraph.md)
- [class MDLMaterialPropertyNode](mdlmaterialpropertynode.md)
- [class MDLScatteringFunction](mdlscatteringfunction.md)
  A set of material properties that describes a basic shading model for materials, and the superclass for more complex shading models.
- [class MDLPhysicallyPlausibleScatteringFunction](mdlphysicallyplausiblescatteringfunction.md)
  A set of material properties that describes a physically realistic shading model for materials.
### Textures
- [class MDLTexture](mdltexture.md)
  A source of texel data to be used in rendering material surface appearances.
- [class MDLCheckerboardTexture](mdlcheckerboardtexture.md)
  A generator of texel data that creates a checkerboard pattern with two specified colors.
- [class MDLColorSwatchTexture](mdlcolorswatchtexture.md)
  A generator of texel data that creates a gradient between two specified colors.
- [class MDLNoiseTexture](mdlnoisetexture.md)
  A generator of texel data that creates a field of random noise.
- [class MDLNormalMapTexture](mdlnormalmaptexture.md)
  A generator of texel data that computes a normal map from a supplied texture.
- [class MDLSkyCubeTexture](mdlskycubetexture.md)
  A generator of texel data that creates cube textures using a physically realistic simulation of the sunlit sky.
- [class MDLURLTexture](mdlurltexture.md)
  A lightweight reference to a URL from which to load texture data.
- [class MDLTextureFilter](mdltexturefilter.md)
  A description of filtering modes for a renderer to use when sampling from a texture.
- [class MDLTextureSampler](mdltexturesampler.md)
  An object that pairs a source of texture data with sampling parameters to be used in rendering the texture.
### Lights
- [class MDLLight](mdllight.md)
  The abstract superclass for objects that describe light sources in a scene.
- [class MDLAreaLight](mdlarealight.md)
  A light source that illuminates a 3D scene from an area with a specific shape.
- [class MDLLightProbe](mdllightprobe.md)
  A light source described in terms of the variations in color and intensity of its illumination in all directions.
- [protocol MDLLightProbeIrradianceDataSource](mdllightprobeirradiancedatasource.md)
  Adopt this protocol to provide information for use in automatic placement of light probes around a scene.
- [class MDLPhotometricLight](mdlphotometriclight.md)
  A light source whose shape, direction, and intensity of illumination are determined by a photometric profile.
- [class MDLPhysicallyPlausibleLight](mdlphysicallyplausiblelight.md)
  A light source for use in shading models based on real-world physics.
### Cameras
- [class MDLCamera](mdlcamera.md)
  A point of view for rendering a 3D scene, along with a set of parameters describing an intended appearance for rendering.
- [class MDLStereoscopicCamera](mdlstereoscopiccamera.md)
  A point of view for rendering a stereoscopic display of a 3D scene.
### Extensible Asset Format Support
- [protocol MDLComponent](mdlcomponent.md)
  The base protocol for extensible file format support in Model I/O.
- [class MDLObjectContainer](mdlobjectcontainer.md)
  A default implementation for handling object hierarchy relationships in a 3D asset.
- [protocol MDLObjectContainerComponent](mdlobjectcontainercomponent.md)
  The general interface for classes that can act as containers in an object hierarchy.
- [protocol MDLTransformComponent](mdltransformcomponent.md)
  The general interface for classes that manage local coordinate space transforms for 3D objects
### Volumetric Representations
- [class MDLVoxelArray](mdlvoxelarray.md)
  A model of a 3D object’s solid volume as a collection of , or cubic units.
### Reference
- [Model I/O Data Types](model-i-o-data-types.md)
- [Model I/O Structures](model-i-o-structures.md)
- [Model I/O Enumerations](model-i-o-enumerations.md)
- [Model I/O Constants](model-i-o-constants.md)
### Classes
- [class MDLAnimatedMatrix4x4](mdlanimatedmatrix4x4.md)
- [class MDLAnimatedQuaternion](mdlanimatedquaternion.md)
- [class MDLAnimatedQuaternionArray](mdlanimatedquaternionarray.md)
- [class MDLAnimatedScalar](mdlanimatedscalar.md)
- [class MDLAnimatedScalarArray](mdlanimatedscalararray.md)
- [class MDLAnimatedValue](mdlanimatedvalue.md)
- [class MDLAnimatedVector2](mdlanimatedvector2.md)
- [class MDLAnimatedVector3](mdlanimatedvector3.md)
- [class MDLAnimatedVector3Array](mdlanimatedvector3array.md)
- [class MDLAnimatedVector4](mdlanimatedvector4.md)
- [class MDLAnimationBindComponent](mdlanimationbindcomponent.md)
- [class MDLBundleAssetResolver](mdlbundleassetresolver.md)
- [class MDLMatrix4x4Array](mdlmatrix4x4array.md)
- [class MDLPackedJointAnimation](mdlpackedjointanimation.md)
- [class MDLPathAssetResolver](mdlpathassetresolver.md)
- [class MDLRelativeAssetResolver](mdlrelativeassetresolver.md)
- [class MDLSkeleton](mdlskeleton.md)
- [class MDLTransformMatrixOp](mdltransformmatrixop.md)
- [class MDLTransformOrientOp](mdltransformorientop.md)
- [class MDLTransformRotateOp](mdltransformrotateop.md)
- [class MDLTransformRotateXOp](mdltransformrotatexop.md)
- [class MDLTransformRotateYOp](mdltransformrotateyop.md)
- [class MDLTransformRotateZOp](mdltransformrotatezop.md)
- [class MDLTransformScaleOp](mdltransformscaleop.md)
- [class MDLTransformStack](mdltransformstack.md)
- [class MDLTransformTranslateOp](mdltransformtranslateop.md)
- [class MDLUtility](mdlutility.md)
### Protocols
- [protocol MDLAssetResolver](mdlassetresolver.md)
- [protocol MDLJointAnimation](mdljointanimation.md)
- [protocol MDLTransformOp](mdltransformop.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/ModelIO)*