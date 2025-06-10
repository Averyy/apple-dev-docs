# removeResidencySet(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Removes a residency set from the command queue.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func removeResidencySet(_ residencySet: any MTLResidencySet)
```

#### Discussion

After calling this method ensures only the remaining residency sets remain resident during the execution of the command buffers you commit this command queue.

## Parameters

- `residencySet`:   instance to remove from the command queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandqueue/removeresidencyset(_:))*