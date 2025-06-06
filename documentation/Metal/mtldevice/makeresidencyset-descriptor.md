# makeResidencySet(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a residency set, which can move resources in and out of memory residency.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func makeResidencySet(descriptor desc: MTLResidencySetDescriptor) throws -> any MTLResidencySet
```

## Mentions

- [Simplifying GPU Resource Management with Residency Sets](simplifying-gpu-resource-management-with-residency-sets.md)

#### Return Value

A new [`MTLResidencySet`](mtlresidencyset.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

#### Discussion

Create an [`MTLResidencySet`](mtlresidencyset.md) by creating and configuring an [`MTLResidencySetDescriptor`](mtlresidencysetdescriptor.md) instance and pass it to this method.

See [`Simplifying GPU Resource Management with Residency Sets`](simplifying-gpu-resource-management-with-residency-sets.md) for more information.

## Parameters

- `desc`: A descriptor instance that configures the residency set the method creates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makeresidencyset(descriptor:))*