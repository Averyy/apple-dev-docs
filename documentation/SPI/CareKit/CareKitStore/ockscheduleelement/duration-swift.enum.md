---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockscheduleelement/duration-swift.enum"
framework: "CareKit/CareKitStore"
---

# OCKScheduleElement.Duration

**Framework**: CareKit/CareKitStore  
**Kind**: enum  
**Role**: Enumeration

A duration describing the length of an event. Options include all day, or a deterministic number of hours, minutes, or seconds.

## Declaration

```swift
enum Duration
```

## Topics

### Enumeration Cases
- [OCKScheduleElement.Duration.allDay](./duration-swift.enum/allday.md)
  Describes an duration that fills an entire date
- [OCKScheduleElement.Duration.seconds(_:)](./duration-swift.enum/seconds%28_%29.md)
  Describes a fixed duration in seconds
### Initializers
- [init(from: Decoder) throws](./duration-swift.enum/init%28from%29.md)
### Instance Methods
- [func encode(to: Encoder) throws](./duration-swift.enum/encode%28to%29.md)
### Type Methods
- [static func hours(Double) -> Duration](./duration-swift.enum/hours%28_%29.md)
  Creates a duration that represents a given number of hours.
- [static func minutes(Double) -> Duration](./duration-swift.enum/minutes%28_%29.md)
  Creates a duration that represents a given number of minutes.
### Default Implementations
- [Equatable Implementations](./duration-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockscheduleelement/duration-swift.enum)*