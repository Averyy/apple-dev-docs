# waitForEvent(_:value:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Schedules an operation to wait for a GPU event of a specific value before continuing to execute any future GPU work.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func waitForEvent(_ event: any MTLEvent, value: UInt64)
```

## Parameters

- `event`:   to wait on.
- `value`: The specific value to wait for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandqueue/waitforevent(_:value:))*