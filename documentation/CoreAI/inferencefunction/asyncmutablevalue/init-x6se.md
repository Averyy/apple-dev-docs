# init(_:)

**Framework**: Core AI  
**Kind**: init

Initialize the state from an existing ndArray.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(_ ndArray: consuming NDArray)
```

#### Discussion

> **Note**: The ndArray will be eagerly copied if not uniquely referenced.

## Parameters

- `ndArray`: The starting ndArray value of this state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/asyncmutablevalue/init(_:)-x6se)*