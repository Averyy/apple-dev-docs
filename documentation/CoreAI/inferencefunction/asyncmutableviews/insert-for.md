# insert(_:for:)

**Framework**: Core AI  
**Kind**: method

Insert the view to be used as the async mutable value for `name`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
mutating func insert(_ mutableValue: inout InferenceFunction.AsyncMutableValue, for name: String)
```

## Parameters

- `mutableValue`: The mutable value that this collection will reference. Its lifetime is tied to the resulting collection.
- `name`: The name of the state or output view being specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/asyncmutableviews/insert(_:for:))*