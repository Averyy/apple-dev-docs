# copyDescription

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Instance Property

The callback used to create a descriptive string representation of the CFFileDescriptor.

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
var copyDescription: ((UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)!
```

```c
const struct __CFString *(*)(void *) copyDescription;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cffiledescriptorcontext/copydescription)*