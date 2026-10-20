# release

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Instance Property

The release callback used by the CFFileDescriptor.

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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cffiledescriptorcontext/release)*