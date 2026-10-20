# Body

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

The type of keyframes representing the body of this type.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
associatedtype Body : Keyframes
```

#### Discussion

When you create a custom keyframes type, Swift infers this type from your implementation of the required [`body`](./body-swift.property.md) property.

## See Also

### Creating a keyframe
- [var body: Self.Body](./body-swift.property.md)
  The composition of content that comprise the keyframes.
- [associatedtype Value = Self.Body.Value](./value.md)
  The type of value animated by this keyframes type


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/keyframes/body-swift.associatedtype)*