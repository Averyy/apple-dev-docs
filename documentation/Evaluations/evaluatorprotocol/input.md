# Input

**Framework**: Evaluations  
**Kind**: associatedtype  
**Required**: Yes

The input sample type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
associatedtype Input : SampleProtocol where Self.Input.ExpectedValue == Self.Subject.Value
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluatorprotocol/input)*