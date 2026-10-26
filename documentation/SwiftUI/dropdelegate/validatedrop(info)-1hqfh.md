# validateDrop(info:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a drop containing items conforming to one of the expected types entered a view that accepts drops.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func validateDrop(info: DropInfo) -> Bool
```

#### Discussion

Specify the expected types when you apply the drop modifier to the view. The default implementation returns `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropdelegate/validatedrop(info:)-1hqfh)*