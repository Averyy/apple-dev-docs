# waitForEvent(_:value:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Schedules an operation to wait for a GPU event of a specific value before continuing to execute any future GPU work.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func waitForEvent(_ event: any MTLEvent, value: UInt64)
```

## Parameters

- `event`:   to wait on.
- `value`: The specific value to wait for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandqueue/waitforevent(_:value:))*