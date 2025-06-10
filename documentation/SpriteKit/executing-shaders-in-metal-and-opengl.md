# Executing Shaders in Metal and OpenGL

**Framework**: SpriteKit

Toggle between renderers to make sure your shader code compiles in both the Metal and OpenGL environments.

#### Overview

On devices that support it, the GLSL code you provide to [`SKShader`](skshader.md) is automatically converted to Metal shading language and run on a Metal renderer. On older devices, shader code is run in OpenGL. It’s important to be mindful of this for debugging purposes because some issues may appear in one renderer but not the other.

You can specify which renderer your device uses—for example, forcing a Metal-enabled device to use SpriteKit’s OpenGL renderer for debugging purposes—by adding a `PrefersOpenGL` to your app’s `Info.plist` key with a value of `true`. See [`Requesting the OpenGL Renderer`](requesting-the-opengl-renderer.md) for more information.

> ❗ **Important**:  To ensure compatibility across all devices, test your shader code with and without the `PrefersOpenGL` key, to be certain it compiles in both environments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/executing-shaders-in-metal-and-opengl)*