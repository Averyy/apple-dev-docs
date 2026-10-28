# Simulating particles in your visionOS app

**Framework**: RealityKit  
**Role**: Sample Code  
**Download**: [SimulatingParticlesInYourVisionOSApp.zip](https://docs-assets.developer.apple.com/published/24672e0aad03/SimulatingParticlesInYourVisionOSApp.zip)

Add a range of visual effects to a RealityKit view by attaching a particle emitter component to an entity.

**Availability**:
- visionOS 1.0+
- Xcode 15.3+

## Overview

Define and tailor a particle system by creating and configuring a particle emitter component and then adding it to an entity. A particle emitter component can simulate various effects including fire, smoke, confetti, and so on.

The sample app presents sliders, toggles, buttons, and color pickers that adjust the particle emitter’s settings. You change the appearance and behavior of the particles it emits with these controls, including their size, shape, and speed.

[Video: A large visionOS window with a blurred glass background, displaying particles flowing from the bottom to the center. The particles are transitioning between pink and purple.](https://developer.apple.com/tutorials/videos/com.apple.RealityKit/particles-main.mp4)

The app’s controls let you quickly try a variety of particle effects that illustrate the range of possibilities for your app.

You can add a particle emitter to your RealityKit scene in four steps.

1. Create an entity.
2. Create a particle emitter component.
3. Add that component to the entity.
4. Add the entity to a scene.

### Create an entity

You can turn any entity into a particle emitter, including one that’s already in your app’s scene. The app creates a new entity with the default initializer [`init()`](./entity/init%28%29.md).

```swift
let emitterEntity = Entity()
```

### Create a particle emitter component

Create a [`ParticleEmitterComponent`](./particleemittercomponent.md) instance by calling one of its initializers.

```swift
var emitterComponent = ParticleEmitterComponent()
```

You can also create a particle emitter from a preset by accessing one of the properties of the [`ParticleEmitterComponent.Presets`](./particleemittercomponent/presets.md) type.

```swift
typealias Presets = ParticleEmitterComponent.Presets

switch presetSelection {
    case .default:
        emitterComponent = ParticleEmitterComponent()
    case .fireworks:
        emitterComponent = Presets.fireworks
    case .impact:
        emitterComponent = Presets.impact
    case .magic:
        emitterComponent = Presets.magic
    case .rain:
        emitterComponent = Presets.rain
    case .snow:
        emitterComponent = Presets.snow
    case .sparks:
        emitterComponent = Presets.sparks
}
```

Each preset is an initial configuration that sets up a new particle emitter system.

**Fireworks**:

[Video: A screen capture of a particle emitter with particles in the form of fireworks that project upward from the bottom of a visionOS window, and then explode near the top.](https://developer.apple.com/tutorials/videos/com.apple.RealityKit/particles-presets-fireworks.mp4)

**Impact**:

[Video: A screen capture of a particle emitter with particles that emit in a radial pattern and simulate dust from an object hitting the ground.](https://developer.apple.com/tutorials/videos/com.apple.RealityKit/particles-presets-impact.mp4)

**Magic**:

[Video: A screen capture of a particle emitter with particles that twinkle and emit spawn particles.](https://developer.apple.com/tutorials/videos/com.apple.RealityKit/particles-presets-magic.mp4)

**Rain**:

[Video: A screen capture of a particle emitter with particles that move downwards fast, and are semi-opaque, rendered as streaks.](https://developer.apple.com/tutorials/videos/com.apple.RealityKit/particles-presets-rain.mp4)

**Snow**:

[Video: A screen capture of a particle emitter with particles that softly fall, and incorporate motion from a noise pattern.](https://developer.apple.com/tutorials/videos/com.apple.RealityKit/particles-presets-snow.mp4)

**Sparks**:

[Video: A screen capture of a particle emitter with particles projecting from the bottom left side. The particles are quick and short lived particles that accumulate color to simulate welding sparks.](https://developer.apple.com/tutorials/videos/com.apple.RealityKit/particles-presets-sparks.mp4)

You can use a preset as a starting point and then alter the behavior and appearance of the emitter and its particles by modifying the component’s properties. This approach may be more convenient than configuring every property of a particle emitter component.

### Add a particle emitter component to an entity

Add the particle emitter  component to an entity by calling the [`set(_:)`](./entity/componentset/set%28_%29-8sii2.md) method of its [`components`](./entity/components.md) property.

```swift
// Add the particle component to the entity.
emitterEntity.components.set(emitterComponent)
```

### Add the entity to a scene

Add the entity with the particle emitter component to the scene by calling the [`add(_:)`](./realityviewcontentprotocol/add%28_%29.md) method of the [`RealityViewContent`](./realityviewcontent.md) instance from a [`RealityView`](./realityview.md).

```swift
// Add the emitter entity to the scene.
content.add(emitterEntity)
```

The scene can now present the entity as a particle emitter because it has the component that defines the look and behavior of the emitter and the particles it creates.

[Video: A large visionOS window with a blurred glass background, displaying pink particles flowing from the bottom to the top.](https://developer.apple.com/tutorials/videos/com.apple.RealityKit/particles-base.mp4)

### Configure the behavior of the emitter’s particles

You can alter the behavior of a particle system by changing the values of a [`ParticleEmitterComponent`](./particleemittercomponent.md) instance’s properties. For example, the [`speed`](./particleemittercomponent/speed.md) property adjusts the starting speed of the particles as the emitter creates them, and the [`birthRate`](./particleemittercomponent/particleemitter/birthrate.md) property modifies how many times per second the emitter creates a new particle.

```swift
emitterComponent.speed = 0.2
emitterComponent.mainEmitter.birthRate = 150

emitterEntity.components.set(emitterComponent)
```

This example modifies the component’s `speed` and `birthrate` properties to `0.2` and `150`, respectively, from their default values `0.5` and `100`, which creates more particles that move slower.

[Video: A screen capture of a particle emitter that's producing pink particles that flow from the bottom of a visionOS window to its center.](https://developer.apple.com/tutorials/videos/com.apple.RealityKit/particles-dense.mp4)

> ❗ **Important**: If you adjust one or more particle component properties, you need to replace the entity’s current particle component instance by setting it again because component instances are from value types.

### Configure the color for the emitter’s particles

You can customize the color of the particles an emitter component creates by setting the [`color`](./particleemittercomponent/particleemitter/color-swift.property.md) property to one of the enumeration cases, including:

- [`ParticleEmitterComponent.ParticleEmitter.ParticleColor.constant(_:)`](./particleemittercomponent/particleemitter/particlecolor/constant%28_%29.md)
- [`ParticleEmitterComponent.ParticleEmitter.ParticleColor.evolving(start:end:)`](./particleemittercomponent/particleemitter/particlecolor/evolving%28start,end%29.md)

A particle with a constant color maintains the same color throughout its lifetime, but a particle with an evolving color gradually changes from one color to another over the duration of its lifetime.

The app has two methods that configure particles with a constant color. The `setConstantColor(_:)` method creates a [`ParticleEmitterComponent.ParticleEmitter.ParticleColor.ColorValue`](./particleemittercomponent/particleemitter/particlecolor/colorvalue.md) instance by passing the color a person selects in the app’s UI to the [`ParticleEmitterComponent.ParticleEmitter.ParticleColor.ColorValue.single(_:)`](./particleemittercomponent/particleemitter/particlecolor/colorvalue/single%28_%29-58m53.md) enumeration case, and then creates a constant color from that value.

```swift
typealias ParticleEmitter = ParticleEmitterComponent.ParticleEmitter
typealias ParticleColor = ParticleEmitter.ParticleColor
typealias ParticleColorValue = ParticleColor.ColorValue

// ...

func setConstantColor(_ swiftUIColor: SwiftUI.Color) {
    // Create a single color value instance.
    let color1 = ParticleEmitter.Color(swiftUIColor)
    let singleColorValue = ParticleColorValue.single(color1)

    // Create a constant color from the single color value.
    let constantColor = ParticleColor.constant(singleColorValue)

    // Change the particle color for the emitter.
    emitterComponent.mainEmitter.color = constantColor

    // Replace the entity's emitter component with the current configuration.
    emitterEntity.components.set(emitterComponent)
}
```

The app’s `setRandomColor(_:_:)` method also creates a constant color that’s random by passing two colors from the app’s UI to the [`ParticleEmitterComponent.ParticleEmitter.ParticleColor.ColorValue.random(a:b:)`](./particleemittercomponent/particleemitter/particlecolor/colorvalue/random%28a,b%29-6g22v.md) enumeration case.

```swift
func setRandomColor(_ swiftUIColor1: SwiftUI.Color,
                    _ swiftUIColor2: SwiftUI.Color) {
    // Create a random color value instance between two colors.
    let color1 = ParticleEmitter.Color(swiftUIColor1)
    let color2 = ParticleEmitter.Color(swiftUIColor2)
    let randomColor = ParticleColorValue.random(a: color1, b: color2)

    // Create a constant color from the random color value.
    let constantColor = ParticleColor.constant(randomColor)

    // Change the particle color for the emitter.
    emitterComponent.mainEmitter.color = constantColor

    // Replace the entity's emitter component with the current configuration.
    emitterEntity.components.set(emitterComponent)
}
```

The enumeration case creates a color value from the two input colors by selecting a random interpolation value between them.

The app’s `setEvolvingColor(_:_:)` method configures an emitter’s particles so that they shift from one color to another over time by creating an evolving color.

```swift
func setEvolvingColor(_ swiftUIColor1: SwiftUI.Color,
                      _ swiftUIColor2: SwiftUI.Color) {

    // Create two single color value instances.
    let color1 = ParticleEmitter.Color(swiftUIColor1)
    let color2 = ParticleEmitter.Color(swiftUIColor2)
    let singleColorValue1 = ParticleColorValue.single(color1)
    let singleColorValue2 = ParticleColorValue.single(color2)

    // Create an evolving color that shifts from one color value to another.
    let evolvingColor = ParticleColor.evolving(start: singleColorValue1,
                                               end: singleColorValue2)

    // Change the particle color for the emitter.
    emitterComponent.mainEmitter.color = evolvingColor

    // Replace the entity's emitter component with the current configuration.
    emitterEntity.components.set(emitterComponent)
}
```

The method creates an evolving color by passing two single color value instances to the [`ParticleEmitterComponent.ParticleEmitter.ParticleColor.evolving(start:end:)`](./particleemittercomponent/particleemitter/particlecolor/evolving%28start,end%29.md) enumeration case.

**Constant single color**:

[Video: A screen recording of the app's particle emitter producing red particles, which flow upward from the bottom of the app's window in visionOS.](https://developer.apple.com/tutorials/videos/com.apple.RealityKit/particles-color-one.mp4)

**Constant random color**:

[Video: A screen recording of the app's particle emitter producing particles, each of which is a random shade of purple because a person selected red and blue colors in the app's UI. The particles flow upward from the bottom of the app's window in visionOS.](https://developer.apple.com/tutorials/videos/com.apple.RealityKit/particles-color-random.mp4)

**Evolving color**:

[Video: A screen recording of the app's particle emitter producing particles that transition from one color to another as they flow upward from the bottom of the app's window in visionOS.](https://developer.apple.com/tutorials/videos/com.apple.RealityKit/particles-color-evolve.mp4)

### Customize the appearance of the emitter’s particles with images

The app lets a person change the appearance of the emitter’s particles by applying an image to each. It does this by creating a [`TextureResource`](./textureresource.md) instance from an image and assigning it to the emitter’s [`image`](./particleemittercomponent/particleemitter/image.md) property.

```swift
emitterComponent.mainEmitter.image = textureResource
```

You can create a texture resource by loading an image from the app’s bundle with the [`load(named:in:)`](./textureresource/load%28named,in%29.md) method, or by passing a [`CGImage`](../CoreGraphics/cgimage.md) instance to the [`generate(from:withName:options:)`](./textureresource/generate%28from,withname,options%29.md) factory method.

The app generates a texture resource in its `generateTextureFromSystemName(_:)` method by taking these steps:

1. Retrieve a symbol from SF Symbols using the symbol’s name.
2. Draw the image as a template onto a white background in a graphics context.
3. Retrieve the image from the context.
4. Pass the final image to the texture resource type’s factory method.

```swift
func generateTextureFromSystemName( _ name: String) -> TextureResource? {
    let imageSize = CGSize(width: 128, height: 128)
    
    // Create a UIImage from a symbol name.
    guard var symbolImage = UIImage(systemName: name) else {
        return nil
    }

    // Create a new version that always uses the template rendering mode.
    symbolImage = symbolImage.withRenderingMode(.alwaysTemplate)

    // Start the graphics context.
    UIGraphicsBeginImageContextWithOptions(imageSize, false, 0)

    // Set the color's texture to white so that the app can apply a color
    // on top of the image.
    UIColor.white.set()

    // Draw the image with the context.
    let rectangle = CGRect(origin: CGPoint.zero, size: imageSize)
    symbolImage.draw(in: rectangle, blendMode: .normal, alpha: 1.0)

    // Retrieve the image from the context.
    let contextImage = UIGraphicsGetImageFromCurrentImageContext()

    // End the graphics context.
    UIGraphicsEndImageContext()

    // Retrieve the Core Graphics version of the image.
    guard let coreGraphicsImage = contextImage?.cgImage else {
        return nil
    }

    // Generate the texture resource from the Core Graphics image.
    let creationOptions = TextureResource.CreateOptions(semantic: .raw)
    return try? TextureResource.generate(from: coreGraphicsImage,
                                         options: creationOptions)
}
```

The method makes a texture resource that works with the emitter’s current color by starting with all white before drawing the image onto it.

The app presents a slider that changes the [`angleVariation`](./particleemittercomponent/particleemitter/anglevariation.md) property. In the example below, the slider’s value is `.pi / 6` radians, which is equivalent to 30º.

[Video: A screen recording of the app's particle emitter producing particles that have the shape of a yellow triangle with an exclamation mark in the center. Each particle has a random rotation between 30 degrees clockwise and 30 degrees counterclockwise because a person set the angle-variation slider in the app's UI to 30 degrees.](https://developer.apple.com/tutorials/videos/com.apple.RealityKit/particles-alert.mp4)

## See Also

### Particle simulation
- [struct ParticleEmitterComponent](./particleemittercomponent.md)
  A component that emits particles.
- [ParticleEmitterComponent.ParticleEmitter](./particleemittercomponent/particleemitter.md)
- [ParticleEmitterComponent.Presets](./particleemittercomponent/presets.md)
  Initial configurations that can be set when starting a new simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/simulating-particles-in-your-visionos-app)*