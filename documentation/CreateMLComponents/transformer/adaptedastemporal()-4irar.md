# adaptedAsTemporal()

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Exposes this transformer as a temporal transformer.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
func adaptedAsTemporal() -> TransformerToTemporalAdaptor<Self>
```

**Other overloads**:

```swift
@preconcurrency
func adaptedAsTemporal() -> TemporalAdaptor<Self> where Self : Sendable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformer/adaptedastemporal()-4irar)*