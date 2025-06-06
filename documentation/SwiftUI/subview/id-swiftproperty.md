# id

**Framework**: SwiftUI  
**Kind**: property

The unique identifier of the view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var id: Subview.ID { get }
```

#### Discussion

This identifier persists across updates, changes to the order of subviews, etc. so can be used to track the lifetime of a subview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/subview/id-swift.property)*