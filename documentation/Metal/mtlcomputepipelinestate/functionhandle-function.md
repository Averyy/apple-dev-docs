# functionHandle(function:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a function handle for a visible function.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func functionHandle(function: any MTLFunction) -> (any MTLFunctionHandle)?
```

#### Return Value

A handle to the visible function. When this value is `nil`, an error occurred during handle creation.

## Parameters

- `function`: An   instance that represents the visible function to create a handle for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/functionhandle(function:))*