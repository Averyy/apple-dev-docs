# events(matching:)

**Framework**: Accessory Access  
**Kind**: method

Returns an asynchronous list of events that match the provided criteria.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func events(matching criteria: [AAUSBAccessoryMatchingCriteria]) async throws -> some AsyncSequence<AAUSBAccessory.Event, Never>
```

## Parameters

- `criteria`: An array of [`AAUSBAccessoryMatchingCriteria`](aausbaccessorymatchingcriteria.md) to use to filter events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aausbaccessorymanager/events(matching:))*