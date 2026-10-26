---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/compiledtrace"
framework: "mlx-swift-lm/MLXLMCommon"
---

# CompiledTrace

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

A compiled trace of a body that reads module weights.

## Declaration

```swift
final class CompiledTrace<Owner> where Owner : Module
```

#### Overview

The declared modules’ weights become compile `inputs:`, so every call reads their current values instead of the ones the first call happened to see. Without that, a compiled forward silently ignores a loaded adapter or a training step.

The body takes its owner as a parameter and is `@Sendable`, so it cannot reach the weights any other way: capturing `self` does not compile.

```swift
final class MoEBlock: Module, UnaryLayer {
    // The body stays inside this module, so the default state covers it.
    private let compiledForward = CompiledTrace<MoEBlock> { block, arguments in
        [block.forward(arguments[0])]
    }

    func callAsFunction(_ x: MLXArray) -> MLXArray {
        compiledForward(self, x)
    }
}
```

Compilation is lazy, so a module can create its traces in `init` and they still read weights loaded later. Traces never retain their owner.

A trace is built from the modules present when it first ran, so replacing modules invalidates it: see `Module.invalidateCompiledTraces()`.

## Topics

### Initializers
- [init(state: StateProvider, body: Body)](./compiledtrace/init%28state,body%29.md)
### Instance Properties
- [var isCompiled: Bool](./compiledtrace/iscompiled.md)
  Whether the trace has been compiled.
### Instance Methods
- [func callAsFunction(Owner, MLXArray) -> MLXArray](./compiledtrace/callasfunction%28_,_%29-2w09h.md)
  Convenience for a single argument and a single result.
- [func callAsFunction(Owner, [MLXArray]) -> [MLXArray]](./compiledtrace/callasfunction%28_,_%29-47ffm.md)
  Runs the trace, compiling it on first use.
- [func invalidate()](./compiledtrace/invalidate%28%29.md)
  Drops the compiled trace; the next call re-reads the module tree.
### Type Aliases
- [CompiledTrace.Body](./compiledtrace/body.md)
  The traced body. Receives the owner whose weights it may read.
- [CompiledTrace.StateProvider](./compiledtrace/stateprovider.md)
  Returns the modules whose weights the body reads.

## Relationships

### Conforms To
- [CompiledTraceInvalidating](./compiledtraceinvalidating.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/compiledtrace)*