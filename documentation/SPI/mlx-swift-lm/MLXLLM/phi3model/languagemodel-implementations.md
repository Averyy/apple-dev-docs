---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/phi3model/languagemodel-implementations"
framework: "mlx-swift-lm/MLXLLM"
---

# LanguageModel Implementations

**Framework**: mlx-swift-lm/MLXLLM  
**Role**: API Collection

## Topics

### Instance Methods
- [func cacheStatus(parameters: GenerateParameters?) throws -> KVCacheStatus](./cachestatus%28parameters%29.md)
- [func callAsFunction(LMInput.Text, cache: [any KVCache]?, state: LMOutput.State?) -> LMOutput](./callasfunction%28_,cache,state%29.md)
- [func fuse(with: any ModelAdapter) throws](./fuse%28with%29.md)
- [func load(adapter: any ModelAdapter) throws](./load%28adapter%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [any KVCache]](./newcache%28parameters%29.md)
- [func nextTokenLogits(LMInput.Text, cache: [any KVCache]?, state: LMOutput.State?) -> LMOutput](./nexttokenlogits%28_,cache,state%29.md)
- [func perform<R>(with: any ModelAdapter, perform: () async throws -> R) async throws -> R](./perform%28with,perform%29-266iy.md)
- [func perform<R>(with: any ModelAdapter, perform: () throws -> R) throws -> R](./perform%28with,perform%29-9lu07.md)
- [func prepare() throws](./prepare%28%29.md)
- [func prepare(LMInput, cache: [any KVCache], state: LMOutput.State?, windowSize: Int?) throws -> PrepareResult](./prepare%28_,cache,state,windowsize%29.md)
- [func unload(adapter: any ModelAdapter)](./unload%28adapter%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/phi3model/languagemodel-implementations)*