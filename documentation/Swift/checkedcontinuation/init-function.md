# init(_:function:)

**Framework**: Swift  
**Kind**: init

Convert a non-copyable continuation to a [`CheckedContinuation`](checkedcontinuation.md)

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(_ continuation: consuming Continuation<T, E>, function: String = #function)
```

#### Discussion

A checked continuation may be escaped into contexts where the non-copyable semantics would not be able to statically enforce the resume-once semantics, however the correct use of the continuation is enforced in some way at runtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/checkedcontinuation/init(_:function:))*