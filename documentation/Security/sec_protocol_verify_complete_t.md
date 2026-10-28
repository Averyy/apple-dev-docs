# sec_protocol_verify_complete_t

**Framework**: Security  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
typealias sec_protocol_verify_complete_t = (Bool) -> Void
```

```c
typedef void (^)(_Bool) sec_protocol_verify_complete_t;
```

## Discussion

Block to be invoked when verification is complete.

## Parameters

- `result`: A `bool` indicating if verification succeeded or failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sec_protocol_verify_complete_t)*