# finalize()

**Framework**: Foundation  
**Kind**: method

The garbage collector invokes this method on the receiver before disposing of the memory it uses.

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
func finalize()
```

#### Discussion

This method behaves as described in the `NSObject` class specification under the [`finalize()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/finalize()) instance method. Note that a `finalize` method must be thread-safe.

## See Also

- [func dealloc()](nsproxy/dealloc.md)
  Deallocates the memory occupied by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsproxy/finalize())*