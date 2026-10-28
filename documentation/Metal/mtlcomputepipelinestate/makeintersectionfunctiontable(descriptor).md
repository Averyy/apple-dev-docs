# makeIntersectionFunctionTable(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (id<MTLIntersectionFunctionTable>) newIntersectionFunctionTableWithDescriptor:(MTLIntersectionFunctionTableDescriptor *) descriptor;
```

## Return Value

A new intersection function table, or `nil` if an error occurred in creation.

## Parameters

- `descriptor`: An [`MTLIntersectionFunctionTableDescriptor`](../mtlintersectionfunctiontabledescriptor.md) instance that configures the created table.

## See Also

### Creating function tables
- [func makeVisibleFunctionTable(descriptor: MTLVisibleFunctionTableDescriptor) -> (any MTLVisibleFunctionTable)?](./makevisiblefunctiontable%28descriptor%29.md)
  Creates a new visible function table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/makeintersectionfunctiontable(descriptor:))*