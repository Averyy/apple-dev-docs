# dealloc()

**Framework**: Foundation  
**Kind**: method

Deallocates the memory occupied by the receiver.

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
func dealloc()
```

#### Discussion

This method behaves as described in the `NSObject` class specification under the [`dealloc`](https://developer.apple.com/documentation/objectivec/nsobject/1571947-dealloc) instance method.

## See Also

- [func finalize()](nsproxy/finalize.md)
  The garbage collector invokes this method on the receiver before disposing of the memory it uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsproxy/dealloc())*