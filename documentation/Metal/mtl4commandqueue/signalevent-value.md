# signalEvent(_:value:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Schedules an operation to signal a GPU event with a specific value after all GPU work prior to this point is complete.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func signalEvent(_ event: any MTLEvent, value: UInt64)
```

## Parameters

- `event`:   to signal.
- `value`: The value to signal the   with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandqueue/signalevent(_:value:))*