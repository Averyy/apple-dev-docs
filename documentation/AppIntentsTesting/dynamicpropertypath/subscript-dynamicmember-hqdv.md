# subscript(dynamicMember:)

**Framework**: App Intents Testing  
**Kind**: subscript

Accesses a property by name without casting.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
subscript(dynamicMember identifier: String) -> (any IntentValueExpressing)? { get throws }
```

#### Overview

Use this subscript to check for `nil` values and to assign values to intent parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/dynamicpropertypath/subscript(dynamicmember:)-hqdv)*