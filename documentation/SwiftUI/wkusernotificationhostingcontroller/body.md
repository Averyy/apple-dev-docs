# body

**Framework**: SwiftUI  
**Kind**: property

The root view of the view hierarchy to display for your notification interface.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
@MainActor
@preconcurrency var body: Body { get }
```

#### Discussion

Override this property and return the root view of your SwiftUI view hierarchy from your implementation. If you don’t override this property, accessing the default implementation triggers an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wkusernotificationhostingcontroller/body)*