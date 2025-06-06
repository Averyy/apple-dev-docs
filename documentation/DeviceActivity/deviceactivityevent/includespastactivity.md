# includesPastActivity

**Framework**: DeviceActivity  
**Kind**: property

Whether the system takes into account the person’s device activity before your app starts monitoring the event.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var includesPastActivity: Bool { get }
```

#### Discussion

For example, if your app calls [`startMonitoring(_:during:events:)`](deviceactivitycenter/startmonitoring(_:during:events:).md) at 1:30pm with a schedule of 1:00pm to 2:00pm, then this boolean determines whether any activity between 1:00pm and 1:30pm will contribute to its threshold. If set to `true` and the event’s schedule does not start on a round hour (for example, it starts at 1:15pm instead of 1:00pm), the system will include device activity from the start of the nearest round hour (for example, it will still include usage from 1:00pm to 1:15pm).


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityevent/includespastactivity)*