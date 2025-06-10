# release

**Framework**: Foundation  
**Kind**: property

Points to the function that decrements a reference count for the given element, and if the reference count becomes zero, frees the given element. If `NULL`, then nothing is done for reference counting or releasing.

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
var release: ((NSMapTable<AnyObject, AnyObject>, UnsafeMutableRawPointer) -> Void)?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmaptablevaluecallbacks/release)*