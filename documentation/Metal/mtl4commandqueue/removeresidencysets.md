# removeResidencySets(_:)

**Framework**: Metal  
**Kind**: method

Removes multiple residency sets from the command queue.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func removeResidencySets(_ residencySets: [any MTLResidencySet])
```

#### Discussion

After calling this method ensures only the remaining residency sets remain resident during the execution of the command buffers you commit this command queue.

## Parameters

- `residencySets`: A Swift array of   instances to remove from the command queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandqueue/removeresidencysets(_:))*