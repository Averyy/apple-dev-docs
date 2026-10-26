---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelfactorytrampoline"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ModelFactoryTrampoline

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

Protocol for types that can provide ModelFactory instances.

## Declaration

```swift
protocol ModelFactoryTrampoline
```

#### Overview

Not used directly.

This is used internally to provide dynamic lookup of a trampoline – this lets API in MLXLMCommon use code present in MLXLLM:

```swift
public class TrampolineModelFactory: NSObject, ModelFactoryTrampoline {
    public static func modelFactory() -> (any MLXLMCommon.ModelFactory)? {
        LLMModelFactory.shared
    }
}
```

That is looked up dynamically with:

```swift
{
    (NSClassFromString("MLXVLM.TrampolineModelFactory") as? ModelFactoryTrampoline.Type)?
        .modelFactory()
}
```

## Topics

### Type Methods
- [static func modelFactory() -> (any GenericModelFactory<ModelContext, ModelContainer>)?](./modelfactorytrampoline/modelfactory%28%29.md)

## See Also

### Related Documentation
- [class ModelFactoryRegistry](./modelfactoryregistry.md)
  Registry of [`ModelFactory`](./modelfactory.md) trampolines.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelfactorytrampoline)*