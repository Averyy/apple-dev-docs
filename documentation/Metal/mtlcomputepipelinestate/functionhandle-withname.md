# functionHandle(withName:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Gets the function handle for a function this pipeline links at the Metal IR level by name.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func functionHandle(withName name: String) -> (any MTLFunctionHandle)?
```

#### Return Value

A function handle corresponding to the function if the name matches a function in this pipeline state, otherwise `nil`.

## Parameters

- `name`: A string representing the name of the function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/functionhandle(withname:))*