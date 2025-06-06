# Manipulating Reality Composer scenes from code

**Framework**: Realitykit

Make programmatic changes to your scenes at runtime.

#### Overview

Although  behaviors provide a way to add interactivity to your scene without writing code, there are times when the only way to implement functionality is to make changes from code. You can manipulate the objects in your scene in many different ways, including hiding or duplicating them, or changing their location, orientation, and scale.

##### Access Scene Objects

To retrieve specific objects from a scene, first assign each object a name in Reality Composer, using the Properties inspector. If you give an object a unique name, Xcode automatically creates an accessor property during code generation. For example, if you have an object called Steel Box in a scene named Box that’s contained in a file called `Experience.reality`, you can get a reference to that object by using code like this:

```swift
if let boxScene = try? Experience.loadBox() {
    let box = boxScene.steelBox
    // Do something with box.
}
```

If you give multiple objects in a scene the same name, the generated property returns an array containing all of the objects that share that name.

If you need to load a named object without using generated code, such as when working with downloaded reality files or loading objects created at runtime, you can use the [`findEntity(named:)`](scene/findentity(named:).md) function on the scene entity.

```swift
if let boxScene = try? Experience.loadBox() {
    if let box = boxScene.findEntity(named: "Steel Box") {}
        // Do something with box
    }
}
```

##### Hide and Show Entities

In addition to hiding and showing objects in your scene using behaviors, as described in [`Bringing a Reality Composer scene to life`](bringing-a-reality-composer-scene-to-life.md), you can also use code to hide and show them, by using the [`isEnabled`](entity/isenabled.md) property. If you set an object’s [`isEnabled`](entity/isenabled.md) property to [`false`](https://developer.apple.com/documentation/swift/false), ARKit doesn’t render it and it doesn’t participate in the scene’s physics simulation. If you set it back to [`true`](https://developer.apple.com/documentation/swift/true), ARKit starts rendering the object again and it resumes participating in the physics simulation.

> **Note**: Child objects of the [`isEnabled`](entity/isenabled.md) property inherit its settings, so disabling [`isEnabled`](entity/isenabled.md) also disables all of its children.

##### Transform a Scene Object

You can transform (move, rotate, or scale) objects in a scene by using the [`transform`](entity/transform.md) property of the [`Entity`](entity.md).

To move an object, change the [`translation`](transform/translation.md) value of the transform. For example, to move a scene object 10 cm along the x-axis, use this:

```swift
myEntity.transform.translation += SIMD3<Float>(10, 0, 0)
```

Similarly, to scale an object, modify the [`scale`](transform/scale.md) of the entity’s [`transform`](entity/transform.md) property. For example, you can double the size of an object in your scene like this:

```swift
myEntity.transform.scale *= 2
```

To rotate an object, make changes to the [`rotation`](transform/rotation.md) property of its [`transform`](entity/transform.md). This code shows you how to rotate an object in your scene by 90° on the z-axis:

```swift
// Calculate 90° as radians.
let radians = 90.0 * Float.pi / 180.0

// Create a quaternion that represents a 90° rotation on the z-axis
// and add it to the existing rotation value.
anchorEntity.transform.rotation += simd_quatf(angle: radians, 
                                              axis: SIMD3<Float>(0,0,1))
```

##### Clone an Entity

If you need to create multiple copies of the same object at runtime, avoid loading the entity multiple times, which can cause performance issues. Instead, load a single copy of the entity before you need it, but don’t add it to your scene. When you need a new instance, call the [`clone(recursive:)`](entity/clone(recursive:).md) function on the loaded entity, and then add the clone as a child of a scene anchor.

Here’s an example of cloning an anchored entity and adding it to your [`ARView`](arview.md):

```swift
let copy = myEntity.clone(recursive: true)
```

##### Add Force to an Object

If an object in a scene participates in the physics simulation, you can add force to that object from code by using the [`addForce(_:relativeTo:)`](modelentity/addforce(_:relativeto:).md) method. Provide a vector representing the amount and direction of force to add to the object as the first parameter. Here’s an example of applying force to an object to make it fly away from the camera:

```swift
// Adjusting the forceMultiplier value changes the amount of force applied.
let forceMultiplier = simd_float3(repeating: 10)
ball.addForce(simd_float3(x: cameraForwardVector.x,
                          y: cameraForwardVector.y,
                          z: cameraForwardVector.z) * forceMultiplier,
              relativeTo: nil)
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
- [Adding procedural assets to a scene](adding-procedural-assets-to-a-scene.md)
  Create procedurally generated shape primitives to your Reality Composer scene.
- [Improving the Accessibility of RealityKit Apps](improving-the-accessibility-of-realitykit-apps.md)
  Incorporate assistive technologies in your augmented reality app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/RealityKit/manipulating-reality-composer-scenes-from-code)*