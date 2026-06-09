# ==(_:_:)

**Framework**: App Intents  
**Kind**: op

Returns a Boolean value indicating whether two containers are equal.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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