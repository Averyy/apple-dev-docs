# addResidencySet(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Marks a residency set as part of this command queue.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func addResidencySet(_ residencySet: any MTLResidencySet)
```

#### Discussion

Ensures that Metal makes the residency set resident during the execution of all command buffers you commit to this command queue.

Each command queue supports up to 32 unique residency set instances.

## Parameters

- `residencySet`:   to add to the command queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandqueue/addresidencyset(_:))*