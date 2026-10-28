---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcontext"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ModelContext

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Context of types that work together to provide a [`LanguageModel`](./languagemodel.md) for inference.

## Declaration

```swift
struct ModelContext
```

## Overview

A [`ModelContext`](./modelcontext.md) is created by [`load(from:using:configuration:useLatest:progressHandler:)`](./genericmodelfactory/load%28from,using,configuration,uselatest,progresshandler%29.md). This contains the following:

- [`ModelConfiguration`](./modelconfiguration.md): identifier for the model
- [`LanguageModel`](./languagemodel.md): the model itself, see [`generate(input:cache:state:parameters:context:components:wiredMemoryTicket:tools:)`](./generate%28input,cache,state,parameters,context,components,wiredmemoryticket,tools%29.md)
- [`UserInputProcessor`](./userinputprocessor.md): can convert [`UserInput`](./userinput.md) into [`LMInput`](./lminput.md)
- `Tokenizer` – the tokenizer used by [`UserInputProcessor`](./userinputprocessor.md)

See also [`loadContainer(from:using:configuration:useLatest:progressHandler:)`](./genericmodelfactory/loadcontainer%28from,using,configuration,uselatest,progresshandler%29.md) and [`ModelContainer`](./modelcontainer.md).

## Topics

### Initializers
- [init(configuration: ModelConfiguration, model: any LanguageModel, processor: any UserInputProcessor, tokenizer: any Tokenizer)](./modelcontext/init%28configuration,model,processor,tokenizer%29.md)
### Instance Properties
- [var configuration: ModelConfiguration](./modelcontext/configuration.md)
- [var model: any LanguageModel](./modelcontext/model.md)
- [var processor: any UserInputProcessor](./modelcontext/processor.md)
- [var tokenizer: Tokenizer](./modelcontext/tokenizer.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcontext)*