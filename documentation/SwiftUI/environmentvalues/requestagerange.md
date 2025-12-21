# requestAgeRange

**Framework**: SwiftUI  
**Kind**: property

An environment value that provides a platform configured action for requesting age ranges.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+

## Declaration

```swift
var requestAgeRange: DeclaredAgeRangeAction { get }
```

#### Discussion

This environment property can be called by a [`Button`](Button.md) click or [`onAppear(perform:)`](View/onAppear(perform:).md)  to invoke the declared age range API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/requestagerange)*