---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcontainer/generate(input:parameters:wiredmemoryticket:tools:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# generate(input:parameters:wiredMemoryTicket:tools:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Generate tokens from prepared input, returning an AsyncStream.

## Declaration

```swift
func generate(input: sending consuming LMInput, parameters: GenerateParameters, wiredMemoryTicket: WiredMemoryTicket? = nil, tools: [[String : any Sendable]]? = nil) async throws -> AsyncStream<Generation>
```

## Return Value

An AsyncStream of generation events

## Discussion

This method provides a thread-safe way to generate tokens without needing to use closure-based `perform` calls.

Example:

```swift
let input = try await modelContainer.prepare(input: userInput)
let stream = try modelContainer.generate(input: input, parameters: parameters)
for await generation in stream {
    switch generation {
    case .chunk(let text): print(text)
    case .info(let info): print(info.tokensPerSecond)
    case .toolCall(let call): handleToolCall(call)
    case .rejectedToolCall(let rejection): handleRejectedToolCall(rejection)
    }
}
```

> **Note**: The `sending` parameter indicates the input is transferred (not shared), allowing non-Sendable types like `LMInput` to safely cross isolation boundaries.

## Parameters

- `input`: Prepared language model input (transferred via `sending`)
- `parameters`: Generation parameters
- `wiredMemoryTicket`: Optional wired memory ticket for policy-based coordination
- `tools`: Optional tool schemas used to parse arguments and authorize function names


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcontainer/generate(input:parameters:wiredmemoryticket:tools:))*