# copyDescription

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Instance Property

A copy description callback for your program-defined `info` pointer. Can be `NULL`.

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
var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!
```

```c
const struct __CFString *(*)(const void *) copyDescription;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1/copydescription)*