# makeArgumentTable(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new argument table from an argument table descriptor.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func makeArgumentTable(descriptor: MTL4ArgumentTableDescriptor) throws -> any MTL4ArgumentTable
```

## Mentions

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)

#### Return Value

A [`MTL4ArgumentTable`](mtl4argumenttable.md) instance, or `nil` if the function failed.

## Parameters

- `descriptor`: A   instance that configures the    instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makeargumenttable(descriptor:))*