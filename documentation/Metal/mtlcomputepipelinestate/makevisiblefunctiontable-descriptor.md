# makeVisibleFunctionTable(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new visible function table.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func makeVisibleFunctionTable(descriptor: MTLVisibleFunctionTableDescriptor) -> (any MTLVisibleFunctionTable)?
```

#### Return Value

A new visible function table, or `nil` if an error occurred in creation.

## Parameters

- `descriptor`: An   instance that configures the created table.

## See Also

- [func makeIntersectionFunctionTable(descriptor: MTLIntersectionFunctionTableDescriptor) -> (any MTLIntersectionFunctionTable)?](mtlcomputepipelinestate/makeintersectionfunctiontable(descriptor:).md)
  Creates a new intersection function table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/makevisiblefunctiontable(descriptor:))*