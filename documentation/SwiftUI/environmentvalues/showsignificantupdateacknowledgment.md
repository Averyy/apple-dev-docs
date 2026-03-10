# showSignificantUpdateAcknowledgment

**Framework**: SwiftUI  
**Kind**: property

Presents a system interface to inform people about significant app changes and request their acknowledgment.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
var showSignificantUpdateAcknowledgment: SignificantUpdateAction { get }
```

#### Discussion

Call this action from a [`Button`](Button.md) or [`onAppear(perform:)`](View/onAppear(perform:).md) to inform people about significant app changes that require their acknowledgment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/showsignificantupdateacknowledgment)*