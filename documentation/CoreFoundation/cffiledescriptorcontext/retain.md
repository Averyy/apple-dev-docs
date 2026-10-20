# retain

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Instance Property

The retain callback used by the CFFileDescriptor.

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
var retain: ((UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!
```

```c
void *(*)(void *) retain;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cffiledescriptorcontext/retain)*