# hasSchedule

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether a medication has a schedule set up.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var hasSchedule: Bool { get }
```

```objc
@property (nonatomic, assign, readonly) BOOL hasSchedule;
```

#### Discussion

The value is `true` for medications for which a person has set up reminders and `false` for medications that are only taken as needed.

> **Note**: Scheduled medications can still be taken as needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkuserannotatedmedication/hasschedule)*