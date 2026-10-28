# init(for:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a new accessibility focus state of the type and using the accessibility technologies you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init<T>(for technologies: AccessibilityTechnologies) where Value == T?, T : Hashable
```

**Other overloads**:

```swift
init(for technologies: AccessibilityTechnologies) where Value == Bool
```

## Parameters

- `technologies`: One or more of the available [`AccessibilityTechnologies`](../accessibilitytechnologies.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilityfocusstate/init(for:)-6u87o)*