---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ocktaskevents/append(event:)"
framework: "CareKit/CareKit"
---

# append(event:)

**Framework**: CareKit/CareKit  
**Kind**: method  
**Role**: Instance Method

Append an event. The event will only be appended if it unique.

## Declaration

```swift
@discardableResult
mutating func append(event: OCKAnyEvent) -> (OCKAnyEvent?, Bool)
```

#### Return Value

(Event, true) if the `event` was successfully appended. (event, false) If the `event` already exists. (nil, false) If the provided event’s task has a nil stable identity.

## Parameters

- `event`: The event to append.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ocktaskevents/append(event:))*