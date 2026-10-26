---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ocktaskevents/events(fortask:)"
framework: "CareKit/CareKit"
---

# events(forTask:)

**Framework**: CareKit/CareKit  
**Kind**: method  
**Role**: Instance Method

Get all events that have matching tasks. Two tasks match if they have equal stable identities defined by the `Identifiable` protocol.

## Declaration

```swift
func events(forTask task: OCKAnyTask) -> [OCKAnyEvent]
```

## Parameters

- `task`: Task used to match for the desired events.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ocktaskevents/events(fortask:))*