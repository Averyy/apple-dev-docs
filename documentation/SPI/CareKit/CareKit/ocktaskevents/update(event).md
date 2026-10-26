---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ocktaskevents/update(event:)"
framework: "CareKit/CareKit"
---

# update(event:)

**Framework**: CareKit/CareKit  
**Kind**: method  
**Role**: Instance Method

Update an event with a particular uniqueness definition. The event will be inserted if it does not yet exist.

## Declaration

```swift
@discardableResult
mutating func update(event: OCKAnyEvent) -> OCKAnyEvent?
```

#### Return Value

The event that was updated. The return value will be nil if the event’s task has a nil stable identity.

## Parameters

- `event`: The event used to check for a uniqueness match.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ocktaskevents/update(event:))*