# init(descriptor:)

**Framework**: RealityKit  
**Kind**: init

Compiles a program from the given descriptor.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(descriptor: PortalMaterial.Program.Descriptor) async throws
```

#### Discussion

Compilation translates the descriptor’s shader graph into a Metal function library, bakes in the descriptor’s function constant values, and links the result into a [`PortalMaterial`](portalmaterial.md)-compatible artifact. The work is asynchronous; build programs once during scene setup and reuse them across every material that needs them.

> **Note**: An error if the shader graph is invalid, if a required built-in portal asset can’t be located, or if shader compilation fails.

## Parameters

- `descriptor`: A configuration that pairs a shader graph with initial input values and function constant values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalmaterial/program-swift.struct/init(descriptor:))*