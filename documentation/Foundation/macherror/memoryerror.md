# memoryError

**Framework**: Foundation  
**Kind**: property

During a page fault, the memory object indicated that the data could not be returned.  This failure may be temporary; future attempts to access this same data may succeed, as defined by the memory object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var memoryError: MachError.Code { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/macherror/memoryerror)*