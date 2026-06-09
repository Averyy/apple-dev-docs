# hash(into:)

**Framework**: Swift  
**Kind**: method

Hash the executor identity into the given hasher.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func hash(into hasher: inout Hasher)
```

#### Discussion

This function is available independently from the `Hashable` conformance, allowing back-deployment to older runtimes when implementing `Hashable` in user code


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unownedtaskexecutor/hash(into:))*