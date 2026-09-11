# ==(_:_:)

**Framework**: App Intents  
**Kind**: op

Returns a Boolean value indicating whether two containers are equal.

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
static func == (lhs: IntentValueContainer, rhs: IntentValueContainer) -> Bool
```

#### Return Value

`true` if the containers are equal; otherwise, `false`.

#### Discussion

Two containers are considered equal if their elements are equal, as determined by the `equals(other:)` method of the container elements.

## Parameters

- `lhs`: A container to compare.
- `rhs`: Another container to compare.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentvaluecontainer/==(_:_:))*