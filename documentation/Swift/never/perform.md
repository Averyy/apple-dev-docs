# perform()

**Framework**: Swift  
**Kind**: method

Performs the intent after resolving the provided parameters.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func perform() async throws -> IntentResultContainer<Never, Never, Never, Never>
```

#### Discussion

In the body of this function, validate your parameters and provide the system with information about needed parameter values or user clarification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/never/perform())*