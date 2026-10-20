# makeVisibleFunctionTable(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (id<MTLVisibleFunctionTable>) newVisibleFunctionTableWithDescriptor:(MTLVisibleFunctionTableDescriptor *) descriptor;
```

#### Return Value

A new visible function table, or `nil` if an error occurred in creation.

## Parameters

- `descriptor`: An [`MTLVisibleFunctionTableDescriptor`](../mtlvisiblefunctiontabledescriptor.md) instance that configures the created table.

## See Also

### Creating function tables
- [func makeIntersectionFunctionTable(descriptor: MTLIntersectionFunctionTableDescriptor) -> (any MTLIntersectionFunctionTable)?](./makeintersectionfunctiontable%28descriptor%29.md)
  Creates a new intersection function table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/makevisiblefunctiontable(descriptor:))*