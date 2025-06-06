# setFailureType(to:)

**Framework**: Combine  
**Kind**: method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func setFailureType<E>(to error: E.Type) -> Publishers.Sequence<Elements, E> where E : Error
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/sequence/setfailuretype(to:))*