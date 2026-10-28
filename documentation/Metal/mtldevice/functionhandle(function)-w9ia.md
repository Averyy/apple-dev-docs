# functionHandle(function:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the handle for a binary function from a pipeline state.

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

```objc
- (id<MTLFunctionHandle>) functionHandleWithBinaryFunction:(id<MTL4BinaryFunction>) function;
```

## Return Value

A function handle if the method succeeds, otherwise `nil`.

## Parameters

- `function`: A function that the Metal compiler created with the [`pipelineIndependent`](../mtlfunctionoptions/pipelineindependent.md) setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/functionhandle(function:)-w9ia)*