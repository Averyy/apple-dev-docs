---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/sensoryfeedback(_:trigger:condition:)"
framework: "CareKit/CareKitUI"
---

# sensoryFeedback(_:trigger:condition:)

**Framework**: CareKit/CareKitUI  
**Kind**: method  
**Role**: Instance Method

Inherited from `View.sensoryFeedback(_:trigger:condition:)`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 26.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func sensoryFeedback<T>(_ feedback: SensoryFeedback, trigger: T, condition: @escaping (T, T) -> Bool) -> some View where T : Equatable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview/sensoryfeedback(_:trigger:condition:))*