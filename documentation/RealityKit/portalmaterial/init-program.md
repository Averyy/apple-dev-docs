# init(program:)

**Framework**: RealityKit  
**Kind**: init

Creates a portal material from a previously compiled program.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(program: PortalMaterial.Program)
```

#### Discussion

Because [`init(descriptor:)`](portalmaterial/program-swift.struct/init(descriptor:).md) is asynchronous, preload the programs your scene needs once during setup, then use this initializer to instantiate portal materials from them synchronously at runtime — for example, when populating a model component each frame.

After creating the material, bind its shader inputs by calling [`setParameter(name:value:)`](portalmaterial/setparameter(name:value:).md) or [`setParameter(handle:value:)`](portalmaterial/setparameter(handle:value:).md).

## Parameters

- `program`: A compiled portal program. The resulting material shares the program’s compiled shader artifact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalmaterial/init(program:))*