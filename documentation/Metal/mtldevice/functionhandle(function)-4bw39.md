# functionHandle(function:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Returns the handle for a function that you can add to a function table.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func functionHandle(function: any MTLFunction) -> (any MTLFunctionHandle)?
```

#### Return Value

A function handle if the method succeeds, otherwise `nil`.

#### Discussion

- [`compileToBinary`](mtlfunctionoptions/compiletobinary.md)
- [`pipelineIndependent`](mtlfunctionoptions/pipelineindependent.md)

## Parameters

- `function`: A function that the Metal compiler created with both of the following settings:


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/functionhandle(function:)-4bw39)*