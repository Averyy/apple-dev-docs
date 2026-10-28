# makeArgumentTable(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a new argument table from an argument table descriptor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func makeArgumentTable(descriptor: MTL4ArgumentTableDescriptor) throws -> any MTL4ArgumentTable
```

```objc
- (id<MTL4ArgumentTable>) newArgumentTableWithDescriptor:(MTL4ArgumentTableDescriptor *) descriptor error:(NSError **) error;
```

## Mentions

- [Understanding the Metal 4 core API](../understanding-the-metal-4-core-api.md)

## Return Value

A [`MTL4ArgumentTable`](../mtl4argumenttable.md) instance, or `nil` if the function failed.

## Parameters

- `descriptor`: A [`MTL4ArgumentTableDescriptor`](../mtl4argumenttabledescriptor.md) instance that configures the [`MTL4ArgumentTable`](../mtl4argumenttable.md) instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makeargumenttable(descriptor:))*