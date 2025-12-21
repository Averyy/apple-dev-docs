# functionHandle(withName:stage:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Obtains a function handle for the a specific function this pipeline links at the Metal IR level.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func functionHandle(withName name: String, stage: MTLRenderStages) -> (any MTLFunctionHandle)?
```

#### Return Value

A function handle representing the function if present, otherwise `nil`.

## Parameters

- `name`: A string containing the name of the function.
- `stage`: The shader stage that uses the function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/functionhandle(withname:stage:))*