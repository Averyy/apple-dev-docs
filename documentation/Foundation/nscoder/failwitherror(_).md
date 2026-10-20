# failWithError(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Signals to this coder that the decode operation has failed.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func failWithError(_ error: any Error)
```

```objc
- (void) failWithError:(NSError *) error;
```

#### Discussion

Typically, you call this method in your [`init(coder:)`](../nscoding/init%28coder%29.md) implementation. You should set the error when you detect problems such as lack of secure coding, data corruption, or a domain validation failure.

This method is only meaningful to call for decodes.

The effect of calling this method depends on the value of [`decodingFailurePolicy`](./decodingfailurepolicy-swift.property.md), as follows:

- If the policy is [`NSCoder.DecodingFailurePolicy.raiseException`](./decodingfailurepolicy-swift.enum/raiseexception.md), calling this method throws an exception immediately. Swift code cannot catch this kind of exception.
- If the policy is [`NSCoder.DecodingFailurePolicy.setErrorAndReturn`](./decodingfailurepolicy-swift.enum/seterrorandreturn.md), calling this method sets the error property once per call to one of the `decode` methods. Calling it repeatedly has no effect until the call stack unwinds to one of these methods’ entry points.

## Parameters

- `error`: An error that indicates why decoding failed.

## See Also

### Managing Decode Errors
- [var error: (any Error)?](./error.md)
  An error in the top-level encode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/failwitherror(_:))*