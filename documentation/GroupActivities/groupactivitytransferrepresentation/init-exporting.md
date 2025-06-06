# init(exporting:)

**Framework**: Group Activities  
**Kind**: init

Creates a type that exports a group activity for the specified item.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init<ActivityType>(exporting: @escaping (Item) async throws -> ActivityType) where ActivityType : GroupActivity
```

## Parameters

- `exporting`: A closure that creates the   for the given item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivitytransferrepresentation/init(exporting:))*