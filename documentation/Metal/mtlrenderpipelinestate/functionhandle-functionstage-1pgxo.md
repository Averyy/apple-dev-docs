# functionHandle(function:stage:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Obtains the function handle for a specific function this pipeline state links at the binary level.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func functionHandle(function: any MTL4BinaryFunction, stage: MTLRenderStages) -> (any MTLFunctionHandle)?
```

#### Return Value

A function handle representing the function if present, otherwise `nil`.

## Parameters

- `function`: A binary function to retrieve the handle.
- `stage`: The shader stage that uses the function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/functionhandle(function:stage:)-1pgxo)*