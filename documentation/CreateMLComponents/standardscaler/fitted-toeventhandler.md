# fitted(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a transformer to a particular input sequence by computing the mean and standard deviation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func fitted<S>(to input: S, eventHandler: EventHandler? = nil) throws -> StandardScaler<Element>.Transformer where Element == S.Element, S : Sequence
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/standardscaler/fitted(to:eventhandler:))*