# children

**Framework**: DeviceActivity  
**Kind**: property

Filters data for the children in the current user’s iCloud family.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
static let children: DeviceActivityFilter.Users
```

#### Discussion

Only parents and guardians in an iCloud family that are actively managing children via the `FamilyControls` framework have permission to report a child’s device activity data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityfilter/users-swift.struct/children)*