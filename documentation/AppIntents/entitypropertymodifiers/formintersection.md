# formIntersection(_:)

**Framework**: App Intents  
**Kind**: method

Removes all elements of this option set that are not also present in the given set.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
mutating func formIntersection(_ other: Self)
```

#### Discussion

This method is implemented as a `&` (bitwise AND) operation on the two sets’ raw values.

## Parameters

- `other`: An option set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entitypropertymodifiers/formintersection(_:))*