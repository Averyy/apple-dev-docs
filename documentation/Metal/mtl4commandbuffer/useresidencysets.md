# useResidencySets(_:)

**Framework**: Metal  
**Kind**: method

Marks an array of residency sets as part of the command buffer’s execution.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func useResidencySets(_ residencySets: [any MTLResidencySet])
```

#### Discussion

Ensures that Metal makes resident the resources that residency sets contain during execution of this command buffer.

## Parameters

- `residencySets`: Array of   instances to mark resident.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandbuffer/useresidencysets(_:))*