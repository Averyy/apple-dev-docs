---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/developing"
framework: "mlx-swift-lm/MLXLMCommon"
---

# Developing mlx-swift-lm

**Framework**: mlx-swift-lm/MLXLMCommon  
**Role**: Article

Techniques for developing *in* mlx-swift-lm.

## Work on Infrastructure

The simplest case for working in mlx-swift-lm is working on infrastructure, e.g. [`KVCache`](./kvcache.md) or [`ToolCallParser`](./toolcallparser.md). You can simply fork mlx-swift-lm and modify the files.  There are unit tests that let you exercise the functionality and you can add more for your specific additions.

The unit tests run without downloading model weights.  There are some tests that exercise the models by using random weights and mock tokenizers, see EvalTests.  This is mostly useful for testing the generation loop itself rather than any particular model.

## Work on Models

If you are working on porting or modifying a model you have a few options:

- use `IntegrationTesting/IntegrationTesting.xcodeproj`
- use `llm-tool` from mlx-swift-examples
- use your own application

### IntegrationTesting

`IntegrationTesting.xcodeproj` integrates with the HuggingFace downloader and tokenizer packages directly and uses MLXHuggingFace macros to adapt their APIs, see [Using mlx-swift-lm](./using.md) for more information. This uses code from `IntegrationTestHelpers` to download weights and run real models.  You can easily change which models it uses or add your own custom tests.

Note: these tests are *not* run in the CI environment, but are a great way to test the models in your own development environment.

### mlx-swift-examples / custom application

You can also test your model by integrating it with a tool or application. This document describes using [llm-tool](https://github.com/ml-explore/mlx-swift-examples/blob/main/Tools/llm-tool/README.md) from `mlx-swift-examples` but the same technique will work with any custom code.

`llm-tool` is a command line tool where you can specify the prompt and the model as arguments when you run it:

```
--model mlx-community/Mistral-7B-Instruct-v0.3-4bit
--prompt "tell me a story"
```

You will want to have mlx-swift-examples (or your own project) open in Xcode with a local checkout of mlx-swift-lm (your fork).  mlx-swift-examples will reference a tagged version of mlx-swift-lm and you need to switch that to reference your local version.  There are two basic methods for doing that (variations on a theme):

- drag the `mlx-swift-lm` *directory* onto the top item (the mlx-swift-examples project) in the Xcode navigator and chose *reference files in place*
- [Xcode documentation](https://developer.apple.com/documentation/xcode/editing-a-package-dependency-as-a-local-package)

In both cases you will get an override of the mlx-swift-lm dependency for this project.  In addition to using your local copy, you can also *edit* mlx-swift-lm at the same time that you use mlx-swift-examples.

For more details on how to configure projects in general, see [Using mlx-swift-lm](./using.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/developing)*