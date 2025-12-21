# maximumResponseTokens

**Framework**: Foundation Models  
**Kind**: property

The maximum number of tokens the model is allowed to produce in its response.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var maximumResponseTokens: Int?
```

#### Discussion

If the model produce `maximumResponseTokens` before it naturally completes its response, the response will be terminated early. No error will be thrown. This property can be used to protect against unexpectedly verbose responses and runaway generations.

If no value is specified, then the model is allowed to produce the longest answer its context size supports. If the response exceeds that limit without terminating, an error will be thrown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationoptions/maximumresponsetokens)*