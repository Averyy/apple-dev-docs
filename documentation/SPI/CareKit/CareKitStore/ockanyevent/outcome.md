---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyevent/outcome"
framework: "CareKit/CareKitStore"
---

# outcome

**Framework**: CareKit/CareKitStore  
**Kind**: property  
**Role**: Instance Property

The outcome for this event.

## Declaration

```swift
let outcome: OCKAnyOutcome?
```

#### Discussion

If the outcome is empty, no actions were recorded.

> **Note**: The outcome may be non-`nil` even if the task didn’t complete. Checking the presence of an outcome isn’t sufficient to determine whether or not the task completed. Here are some examples of times when the outcome is non-`nil` but the task didn’t complete:
>
> - The user created a note specifying why they weren’t able to complete the task.
> - The user completed the task, but then deleted all the values they recorded.
> - The user only partially completed the task.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyevent/outcome)*