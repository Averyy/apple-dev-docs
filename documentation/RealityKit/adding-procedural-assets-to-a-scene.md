# Adding procedural assets to a scene

**Framework**: RealityKit

Create procedurally generated shape primitives to your Reality Composer scene.

#### Overview

RealityKit can generate several types of shape primitives, such as cubes, spheres, and planes. Shape primitives are useful for a variety of debugging and development purposes; for example, you might use them as proxies for unfinished assets. You can also use them instead of artist-created assets for some production purposes. You might, for example, use a generated sphere instead of an artist-modeled ball when creating a sports game.

##### Generate a Mesh Resource

Several [`MeshResource`](meshresource.md) class methods generate instances for different shape primitives. You can use [`MeshResource`](meshresource.md) instances to create entities for your scene.

This code shows you how to generate a procedural, 5-centimeter sphere [`MeshResource`](meshresource.md) using a generator method:

```swift
let sphereResource = MeshResource.generateSphere(radius: 0.05)
```

This code shows an example of creating a box [`MeshResource`](meshresource.md):

```swift
let boxResource = MeshResource.generateBox(size: 0.08)
```

> **Note**: All [`MeshResource`](meshresource.md) generator methods require measurement parameters to be expressed in meters.

##### Define the Appearance of the Procedural Asset

Create a [`Material`](material.md) instance that describes the desired color and other aspects of the procedural asset’s appearance. You typically do so by creating an instance of [`SimpleMaterial`](simplematerial.md).

This example shows you how to display a generated shape with a shiny, metallic-blue surface:

```swift
let myMaterial = SimpleMaterial(color: .blue, roughness: 0, isMetallic: true)
```

##### Create an Entity From a Mesh Resource

You can’t add a generated [`MeshResource`](meshresource.md) asset directly to a [`RealityKit`](RealityKit.md) scene. Instead, generate a [`ModelEntity`](modelentity.md) object based on the asset and pass it as a single-element array to specify the material you created in the previous step.

```swift
let myEntity = ModelEntity(mesh: myMeshResource, materials: [itemMaterial])
```

Once you’ve created a [`ModelEntity`](modelentity.md) that represents your procedural object, place it in your scene by adding it as a descendant of any of your scene’s anchors:

```swift
if let anchor = myScene.findEntity(named: "My Anchor Entity") {
    anchor.addChild(myEntity)
}
```

You can also create a new [`AnchorEntity`](anchorentity.md) to hold your procedural object:

```swift
// Create a new Anchor Entity at the world origin.
let anchorEntity = AnchorEntity(world: .zero)

// Add the entity as a child of the new anchor.
anchorEntity.addChild(myEntity)

// Add the anchor to the scene.
arView.scene.addAnchor(anchorEntity)
```

## See Also

- [Creating 3D Content with Reality Composer](creating-3d-content-with-reality-composer.md)
  Assemble assets into a dynamic 3D composition that you can add to a scene in your app, or share with AR Quick Look.
- [Loading Reality Composer files using generated code](loading-reality-composer-files-using-generated-code.md)
  Leverage automatically generated code to load scenes from Xcode.
- [Loading Reality Composer files manually without generated code](loading-reality-composer-files-manually-without-generated-code.md)
  Load Reality Composer files that aren’t part of your Xcode project.
- [Adding elements to a 3D scene](adding-elements-to-a-3d-scene.md)
  Add assets to your scene from Reality Composer’s library, or import custom assets.
- [Configuring elements in a scene](configuring-elements-in-a-scene.md)
  Define the appearance and behavior of objects in a scene.
- [Arranging elements in a scene](arranging-elements-in-a-scene.md)
  Manipulate objects to complete your Reality Composer scene.
- [Manipulating Reality Composer scenes from code](manipulating-reality-composer-scenes-from-code.md)
  Make programmatic changes to your scenes at runtime.
- [Improving the Accessibility of RealityKit Apps](improving-the-accessibility-of-realitykit-apps.md)
  Incorporate assistive technologies in your augmented reality app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/adding-procedural-assets-to-a-scene)*