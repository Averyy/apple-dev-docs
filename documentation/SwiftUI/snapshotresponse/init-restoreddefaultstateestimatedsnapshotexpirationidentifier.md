# init(restoredDefaultState:estimatedSnapshotExpiration:identifier:)

**Framework**: SwiftUI  
**Kind**: init

Creates a snapshot response.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
init(restoredDefaultState: Bool = false, estimatedSnapshotExpiration: Date? = nil, identifier: String? = nil)
```

## Parameters

- `restoredDefaultState`: Pass   if your app has navigated back   to its default launch scene.
- `estimatedSnapshotExpiration`: The preferred date and time for the   next background snapshot refresh task. Use     if you don’t want to schedule the next refresh.
- `identifier`: A custom string to associate with the next   background snapshot refresh task. This value is assigned to the   next snapshot task’s   userInfo property. Pass   if you   don’t want to associate any identifier with the next task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/snapshotresponse/init(restoreddefaultstate:estimatedsnapshotexpiration:identifier:))*