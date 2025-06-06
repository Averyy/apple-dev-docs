# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Performs the transformation on each element of the input sequence.

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
func applied(to input: some TemporalSequence<Base.Input>, eventHandler: EventHandler? = nil) async throws -> AnyTemporalSequence<TemporalAdaptor<Base>.Output>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporaladaptor/applied(to:eventhandler:))*