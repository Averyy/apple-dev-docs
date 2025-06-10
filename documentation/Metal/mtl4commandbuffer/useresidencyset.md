# useResidencySet(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Marks a residency set as part of the command buffer’s execution.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func useResidencySet(_ residencySet: any MTLResidencySet)
```

#### Discussion

Ensures that Metal makes resident the resources that residency set contains during execution of this command buffer.

## Parameters

- `residencySet`:   instance to mark resident.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandbuffer/useresidencyset(_:))*