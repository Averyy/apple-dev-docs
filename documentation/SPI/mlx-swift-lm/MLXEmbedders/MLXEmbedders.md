---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders"
framework: "mlx-swift-lm/MLXEmbedders"
---

# MLXEmbedders

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: module  
**Role**: Framework

## Topics

### Classes
- [class BertModel](./bertmodel.md)
  The complete BERT model implementation.
- [class BertRerankerModel](./bertrerankermodel.md)
  BERT/RoBERTa-style sequence-classification model used by encoder reranker checkpoints.
- [class BertSequenceClassificationRerankerModel](./bertsequenceclassificationrerankermodel.md)
  BERT sequence-classification model used by reranker checkpoints with pooled-output heads.
- [class DistilBertModel](./distilbertmodel.md)
  A streamlined version of the BERT model.
- [class EmbedderModelContainer](./embeddermodelcontainer.md)
  Container for embedder models that guarantees single threaded access.
- [class EmbedderModelFactory](./embeddermodelfactory.md)
  Factory for creating new Embedder models.
- [class EmbedderRegistry](./embedderregistry.md)
  Registry of known embedder model configurations.
- [class EmbeddingGemma](./embeddinggemma.md)
  A text embedding model based on Gemma 3.
- [class Gemma3ModelBackbone](./gemma3modelbackbone.md)
  The core backbone of the Gemma 3 model.
- [class LFM2BidirectionalModel](./lfm2bidirectionalmodel.md)
  LFM2.5 bidirectional encoder for retrieval. One class serves both heads, selected by the `"mlx"` block in config.json:
- [class NomicBertModel](./nomicbertmodel.md)
  The main entry point for the Nomic BERT model.
- [class Pooling](./pooling.md)
  A module that performs pooling operations on hidden states to produce fixed-sized sentence embeddings.
- [class Qwen3Model](./qwen3model.md)
  The top-level Qwen3 model class providing embedding-level outputs.
### Protocols
- [protocol EmbeddingModel](./embeddingmodel.md)
### Structures
- [struct BertConfiguration](./bertconfiguration.md)
  Configuration parameters for BERT and DistilBERT models.
- [struct EmbedderModelContext](./embeddermodelcontext.md)
  Context of values that work together to provide an [`EmbeddingModel`](./embeddingmodel.md).
- [struct EmbeddingModelOutput](./embeddingmodeloutput.md)
- [struct Gemma3Configuration](./gemma3configuration.md)
  Configuration for the Gemma 3 model.
- [struct LFM2BidirectionalConfiguration](./lfm2bidirectionalconfiguration.md)
- [struct NomicBertConfiguration](./nomicbertconfiguration.md)
  The configuration object defining the hyperparameters and architectural details of Nomic BERT.
- [struct PoolingConfiguration](./poolingconfiguration.md)
  Configuration for the `Pooling` layer, typically loaded from a JSON file.
- [struct Qwen3Configuration](./qwen3configuration.md)
  Configuration for a Qwen3 model.
### Enumerations
- [enum EmbedderTypeRegistry](./embeddertyperegistry.md)
  Registry of model type, e.g ‘bert’, to functions that can instantiate the model from configuration.
### Extended Modules
- [MLX](./mlx.md)
- [MLXLMCommon](./mlxlmcommon.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders)*