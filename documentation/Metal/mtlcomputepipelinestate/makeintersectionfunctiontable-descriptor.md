# makeIntersectionFunctionTable(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new intersection function table.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func makeIntersectionFunctionTable(descriptor: MTLIntersectionFunctionTableDescriptor) -> (any MTLIntersectionFunctionTable)?
```

#### Return Value

A new intersection function table, or `nil` if an error occurred in creation.

## Parameters

- `descriptor`: An   instance that configures the created table.

## See Also

- [func makeVisibleFunctionTable(descriptor: MTLVisibleFunctionTableDescriptor) -> (any MTLVisibleFunctionTable)?](mtlcomputepipelinestate/makevisiblefunctiontable(descriptor:).md)
  Creates a new visible function table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/makeintersectionfunctiontable(descriptor:))*