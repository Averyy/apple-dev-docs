# functionHandle(function:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Gets the function handle for a function this pipeline links at the binary level.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func functionHandle(function: any MTL4BinaryFunction) -> (any MTLFunctionHandle)?
```

#### Return Value

A function handle corresponding to the function if the binary function mathces a function in this pipeline state, otherwise `nil`.

## Parameters

- `function`: A binary function object representing the function binary to find.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/functionhandle(function:)-8spaa)*