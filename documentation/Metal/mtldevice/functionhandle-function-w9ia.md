# functionHandle(function:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Get the function handle for the specified binary-linked function from the pipeline state.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func functionHandle(function: any MTL4BinaryFunction) -> (any MTLFunctionHandle)?
```

#### Return Value

A [`MTLFunctionHandle`](mtlfunctionhandle.md) instance  for a binary function that was compiled with `MTLFunctionOptionPipelineIndependent`, otherwise `nil`.

## Parameters

- `function`: A   instance representing the function binary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/functionhandle(function:)-w9ia)*