# SCNColorMask

**Framework**: SceneKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
struct SCNColorMask
```

```c
enum SCNColorMask : NSInteger;
```

## Topics

### Initializers
- [init(rawValue: Int)](./scncolormask/init%28rawvalue%29.md)
### Type Properties
- [static var all: SCNColorMask](./scncolormask/all.md)
- [static var alpha: SCNColorMask](./scncolormask/alpha.md)
- [static var blue: SCNColorMask](./scncolormask/blue.md)
- [static var green: SCNColorMask](./scncolormask/green.md)
- [static var red: SCNColorMask](./scncolormask/red.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Managing Render Targets
- [var writesToDepthBuffer: Bool](./scnmaterial/writestodepthbuffer.md)
  A Boolean value that determines whether SceneKit produces depth information when rendering the material.
- [var readsFromDepthBuffer: Bool](./scnmaterial/readsfromdepthbuffer.md)
  A Boolean value that determines whether SceneKit uses depth information when rendering the material.
- [var colorBufferWriteMask: SCNColorMask](./scnmaterial/colorbufferwritemask.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncolormask)*