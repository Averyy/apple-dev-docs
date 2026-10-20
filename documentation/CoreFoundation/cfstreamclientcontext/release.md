# release

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Instance Property

A release callback for your program-defined `info` pointer. Can be `NULL`.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var release: ((UnsafeMutableRawPointer?) -> Void)!
```

```c
void (*)(void *) release;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstreamclientcontext/release)*