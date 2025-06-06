# makeCommandQueue(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a command queue with the provided configuration.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func makeCommandQueue(descriptor: MTLCommandQueueDescriptor) -> (any MTLCommandQueue)?
```

## Parameters

- `descriptor`: The configuration for the new command queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makecommandqueue(descriptor:))*