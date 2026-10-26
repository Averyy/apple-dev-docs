---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyoutcome/values"
framework: "CareKit/CareKitStore"
---

# values

**Framework**: CareKit/CareKitStore  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An array of values associated with this outcome.

## Declaration

```swift
var values: [OCKOutcomeValue] { get set }
```

#### Discussion

Most outcomes have 0 or 1 values, but some may have more. For example, a task to call a physician might have 0 values, or 1 value containing the time stamp of when the call was placed.

Another example is a task to walk 2,000 steps that may have 1 value, with that value being the number of steps actually taken. Yet another example is a task to complete a survey that may have multiple values corresponding to the answers to the questions in the survey.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyoutcome/values)*