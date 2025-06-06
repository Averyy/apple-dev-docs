# copyDescription

**Framework**: Core Foundation  
**Kind**: property

A copy description callback for your program-defined `info` pointer. Can be `NULL`.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext/copydescription)*