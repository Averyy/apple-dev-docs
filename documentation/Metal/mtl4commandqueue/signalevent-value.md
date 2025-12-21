# signalEvent(_:value:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Schedules an operation to signal a GPU event with a specific value after all GPU work prior to this point is complete.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func signalEvent(_ event: any MTLEvent, value: UInt64)
```

## Parameters

- `event`:   to signal.
- `value`: The value to signal the   with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandqueue/signalevent(_:value:))*