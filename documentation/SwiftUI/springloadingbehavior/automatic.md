# automatic

**Framework**: SwiftUI  
**Kind**: property

The automatic spring loading behavior.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static let automatic: SpringLoadingBehavior
```

#### Discussion

This defers to default component behavior for spring loading. Some components, such as `TabView`, will default to allowing spring loading; while others do not.

## See Also

- [static let enabled: SpringLoadingBehavior](springloadingbehavior/enabled.md)
  Spring loaded interactions will be enabled for applicable views.
- [static let disabled: SpringLoadingBehavior](springloadingbehavior/disabled.md)
  Spring loaded interactions will be disabled for applicable views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/springloadingbehavior/automatic)*