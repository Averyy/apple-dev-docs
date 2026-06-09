# subscript(dynamicMember:)

**Framework**: App Intents Testing  
**Kind**: subscript

Accesses a property by name without casting.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
subscript(dynamicMember identifier: String) -> (any IntentValueExpressing)? { get throws }
```

#### Overview

Use this subscript to check for `nil` values and to assign values to intent parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/dynamicpropertypath/subscript(dynamicmember:)-hqdv)*