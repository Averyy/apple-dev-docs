# Creating USD files for Apple devices

**Framework**: RealityKit

Generate 3D assets that render as expected.

#### Overview

Universal Scene Description (USD) is a comprehensive 3D content-creation technology that supports a variety of real-time and offline workflows. Depending on the device and its operating system, there are three renderers that might display a 3D asset you create for your real-time apps and AR experiences: RealityKit, SceneKit, or Storm. Each renderer supports a specific subset of the USD features. Use only USD features supported by the renderer that displays your asset to ensure that it renders and functions as desired. For detailed information about which USD features each renderer supports, see [`Validating feature support for USD files`](validating-usd-files.md).

#### Use Metallic Workflows for Shading

All three renderers use a physically based rendering (PBR) technique that the USD specification calls the . A metallic workflow shader takes metallic, roughness, and base color values as its core inputs. Most digital content-creation tools (DCCs) support PBR metallic workflow shaders and many of them default to using it.

USD and many DCCs also support a second PBR technique called the  (sometimes also called the ). The specular workflow renders assets by using another algorithm that takes different input values. Only Storm supports the specular workflow, so for maximum compatibility, use metallic workflow shaders in your DCC, or your preview renders won’t accurately represent how your final rendered asset looks.

> **Note**: Find more information and an example shader implementation for both of USD’s PBR workflows by reading the [`USDPreviewSurface shader page`](https://developer.apple.comhttps://openusd.org/release/spec_usdpreviewsurface.html) in the USD specification.

#### Target a Renderer

Your app or operating system will use one of three renderers, based on these factors:

Use the process outlined below to ensure that your USD assets render correctly and function as expected in your app.

#### Validate Your Usd Assets

USD files that aren’t well-formed may not work correctly. Validate that your assets conform to the USD specification before including them in your app by using OpenUSD’s `usdchecker` command-line tool with the `--arkit` flag. The `usdchecker` command-line tool is available with macOS starting with macOS 15.

#### Use the Latest Usd Schemas

The USD adoption process often results in changes to proposed schemas before they become part of the specification. If you’ve created any assets using a preliminary schema, re-export them using the standard USD schema once the features your asset uses become part of the specification.

> **Note**: Feature support for preliminary schemas will vary by renderer.

#### Target Your Use of Subdivision

USD supports a feature called , which tells the renderer to generate additional geometry on-the-fly to make the entity render more smoothly. Target your use of this feature to instances when you most need smooth rendering. Each level of subdivision increases the number of rendered polygons in the model by a factor of four, which can have substantial performance implications.

> **Note**: The default `subdivisionScheme` value in USD is `catmullClark`, a subdivision surfaces algorithm. This means subdivision surfaces is automatically enabled for assets that don’t explicitly include a subdivision scheme. To ensure that subdivision surfaces is not enabled for your asset, explicitly set `subdivisionScheme` to `none` when exporting from a DCC. For more information, see the [`documentation for GetSubdivisionSchemeAttr() in the USD specification.`](https://developer.apple.comhttps://openusd.org/release/api/class_usd_geom_mesh.html) You can also use the support scripts below to set `subdivisionScheme` to `none` automatically in your USD files.

#### Target Your Use of Double Sided Geometry

USD geometry can be set to render both sides of a surface by setting the `doubleSided` attribute. Target your use of this feature as its support varies by renderer, which may affect how your content is represented, and its performance.

> **Note**: The default `doubleSided` value is off, however some DCCs enable it automatically during export. It is recommended to review your applications export settings to make sure it is only enabled when desired. You can also use the support scripts below to turn off `doubleSided` on your geometry.

#### Limit Rigged Models to a Single Skeleton

USD supports skeletal animation, which you can use to animate a character or other complex model by manipulating a hierarchy of bones or joints to deform the model. Many DCCs allow you to use multiple  (sometimes called  or ), to deform a single mesh. For example, for a character model, you might create one skeleton to handle facial animation and a second one to control general body movement. Before exporting models with multiple skeletons to a USD file, merge all the skeletons into a single joint or bone hierarchy. Models with multiple hierarchies can cause performance and compatibility issues with all three renderers.

> **Note**: All DCCs implement skeletal animation using either a hierarchy of bones or joints. Both approaches deform the model for animation, but use different underlying data representations. DCCs that use bone-based skeletons automatically convert the skeleton to joints when exporting to USD, because USD only supports joint-based skeletons.

#### Include Material and Skeleton Bindings

USD requires that any geometry with an applied material use the `MaterialBindingAPI`. It also requires that any geometry that has a skeleton use the `SkelBindingAPI`. Without these APIs, the material or skeleton information may not be read by an application.

> **Note**: Some DCC versions may not correctly apply these bindings in a USD. You can use the support script below to automatically apply them to geometry that has the attributes.

#### Expose Configurations As Variants

USD supports the ability to have multiple representations of an object using a feature called `variants`. USD files define the primary hierarchy path in the file using the `defaultPrim` metadata. Variants that are defined this `defaultPrim` hierarchy path are shown to the user as configuration options when using QuickLook with USDZ files. The variant configuration interface is available starting with visionOS 2, macOS 15, iOS 18 and iPadOS 18. When a configuration option is selected, the appearance of the USD being viewed in QuickLook will change to respect the selected variant.

> **Note**: Variants can be authored in some DCCs or using the USD API. You can also use the support script below to combine USDZ files into a single file as variants, as long as they only vary in their material or skeleton animations.

#### Use Efficient Textures

Textures are very large contributors to the file size of your content, and its runtime performance.

Use textures that are appropriately sized for your content. Smaller texture sizes help with performance and size, but must be balanced against legibility.

USD files may use a wider range of texture formats, however USDZ files may only include a few texture formats: JPEG, PNG, EXR and AVIF. Use AVIF textures where possible for the best balance between quality and file size.

You can use Preview or the `usdcrush` command line tool to compress the textures within your USDZ file to use AVIF on macOS 26, or JPEG on macOS 15.

#### Converting Dense Meshes

Reduce the number of polygons in your geometry and the number of individual geometry elements to maximize performance.

When using computer aided design (CAD) files, or other dense meshes, you may need to use a DCC to combine geometry elements together and create new topology to reduce the complexity.

> **Note**: Watch [`Optimize your 3D assets forspatial computing`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2024/10186) to learn more about best practices for textures and meshes.

#### Convert Your Models From Other Formats

Use Preview or the `usdcat` command line tool on macOS 26 to convert your models from other common 3D file formats to USD. Both support a range of common file formats like Alembic, OBJ, STL and PLY.

Export directly to USD from your content creation tools when possible, or to one of the supported conversion formats. Unsupported conversion formats will require using a content creation tool to convert them first to USD or another supported conversion format.

> **Note**: PLY files may contain Gaussian Splats information. These will be converted to a preliminary schema to preserve information. This data representation might change in the future as it is further explored in the [`Alliance for OpenUSD`](https://developer.apple.comhttps://aousd.org).

#### Support Scripts

We provide a set of scripts to assist you in creating great USD files, using the OpenUSD Python API. These scripts will help address many of the points above within your USD files, or enable you to create USDZ files using variants.

To download these scripts, see [`USD Support Scripts`](https://developer.apple.comhttps://developer.apple.com/download/files/USD-Support-Scripts.zip).

## Topics

### Validating USD feature support
- [Validating feature support for USD files](validating-usd-files.md)
  Ensure that the renderer that displays your USD assets supports its features.

## See Also

- [Loading entities from a file](loading-entities-from-a-file.md)
  Retrieve an entity from storage on disk using a synchronous or an asynchronous load operation.
- [Stored entities](stored-entities.md)
  Manage entities that you store as assets on disk.
- [convenience(contentsOf:withName:)](entity/init(contentsof:withname:).md)
  Creates an entity by asynchronously loading it from a file URL.
- [convenience(named:in:)](entity/init(named:in:).md)
  Creates an entity by asynchronously loading it from a bundle.
- [struct ReferenceComponent](referencecomponent.md)
  A component that can load another entity from a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/creating-usd-files-for-apple-devices)*