# retain

**Framework**: Foundation  
**Kind**: property

Points to the function that increments a reference count for the given element. If `NULL`, then nothing is done for reference counting.

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
var retain: ((NSHashTable<AnyObject>, UnsafeRawPointer) -> Void)?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshashtablecallbacks/retain)*