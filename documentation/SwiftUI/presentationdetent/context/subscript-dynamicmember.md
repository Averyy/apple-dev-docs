# subscript(dynamicMember:)

**Framework**: SwiftUI  
**Kind**: subscript

Returns the value specified by the keyPath from the environment.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
subscript<T>(dynamicMember keyPath: KeyPath<EnvironmentValues, T>) -> T { get }
```

#### Overview

This uses the environment from where the sheet is shown, not the environment where the presentation modifier is applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/presentationdetent/context/subscript(dynamicmember:))*