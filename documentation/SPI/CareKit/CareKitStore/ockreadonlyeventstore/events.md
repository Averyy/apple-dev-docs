---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadonlyeventstore/events"
framework: "CareKit/CareKitStore"
---

# Events

**Framework**: CareKit/CareKitStore  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

An asynchronous sequence that produces events.

## Declaration

```swift
associatedtype Events : Sendable, AsyncSequence where Self.Events.Element == [OCKEvent<Self.Task, Self.Outcome>]
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadonlyeventstore/events)*