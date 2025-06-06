# fallDetectionManagerDidChangeAuthorization(_:)

**Framework**: Core Motion  
**Kind**: method

Indicates the fall detection authorization status changed.

**Availability**:
- watchOS 7.2+

## Declaration

```swift
optional func fallDetectionManagerDidChangeAuthorization(_ fallDetectionManager: CMFallDetectionManager)
```

#### Discussion

The system calls this method after the fall detection authorization status changes. Check the fall detection manager’s [`authorizationStatus`](cmfalldetectionmanager/authorizationstatus.md) property to determine the current status.

## Parameters

- `fallDetectionManager`: The fall detection manager for the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmfalldetectiondelegate/falldetectionmanagerdidchangeauthorization(_:))*