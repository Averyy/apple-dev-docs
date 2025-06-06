# init(textureSize:forLocation:lightsToConsider:objectsToConsider:reflectiveCubemap:irradianceCubemap:)

**Framework**: Model I/O  
**Kind**: init

Creates a light probe representing the shading environment at a specific point in a scene.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init?(textureSize: Int, forLocation transform: MDLTransform, lightsToConsider: [MDLLight], objectsToConsider: [MDLObject], reflectiveCubemap: MDLTexture?, irradianceCubemap: MDLTexture?)
```

#### Return Value

A new light probe object.

#### Discussion

The behavior of this method changes depending on whether you specify textures for the `reflectiveCubemap` and `irradianceCubemap` parameters.

If the `reflectiveCubemap` parameter is `nil`, this method renders an environment map texture by raytracing a scene containing the lights and meshes (with materials) specified in the `lightsToConsider` and  `objectsToConsider` parameters, using the camera position specified in the `transform` parameter.

If the `irradianceCubemap` parameter is `nil`, this method generates an irradiance texture from the reflective texture (either the texture specified in the `reflectiveCubemap` parameter, or the generated texture if that parameter is `nil`) using the [`MDLTexture`](mdltexture.md) class.

## Parameters

- `textureSize`: The size, in pixels for one side of a cube, of texture image to generate.
- `transform`: The point in a scene at which to generate the light probe.
- `lightsToConsider`: An array of other lights to be used in the shading environment around the generated light probe.
- `objectsToConsider`: An array of scene content—  instances or   instances that contain   instances—to be used in the shading environment around the generated  light probe.
- `reflectiveCubemap`: An optional cube map texture containing the environment as seen from the light probe’s position. Leave this parameter   to generate a reflective texture.
- `irradianceCubemap`: An optional cube map texture containing samples of the total light arriving at the light probe’s position from every direction. Leave this parameter   to generate an irradiance texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdllightprobe/init(texturesize:forlocation:lightstoconsider:objectstoconsider:reflectivecubemap:irradiancecubemap:))*