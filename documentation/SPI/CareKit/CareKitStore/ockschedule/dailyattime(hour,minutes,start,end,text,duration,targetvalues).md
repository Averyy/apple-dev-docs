---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockschedule/dailyattime(hour:minutes:start:end:text:duration:targetvalues:)"
framework: "CareKit/CareKitStore"
---

# dailyAtTime(hour:minutes:start:end:text:duration:targetValues:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Type Method

Create a schedule that happens once per day, every day, at a fixed time.

## Declaration

```swift
static func dailyAtTime(hour: Int, minutes: Int, start: Date, end: Date?, text: String?, duration: OCKScheduleElement.Duration = .hours(1), targetValues: [OCKOutcomeValue] = []) -> OCKSchedule
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockschedule/dailyattime(hour:minutes:start:end:text:duration:targetvalues:))*