# dealloc()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) dealloc;
```

## Discussion

This method behaves as described in the `NSObject` class specification under the [`dealloc`](../../ObjectiveC/nsobject-swift.class/dealloc.md) instance method.

## See Also

### Related Documentation
- [func finalize()](./finalize%28%29.md)
  The garbage collector invokes this method on the receiver before disposing of the memory it uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsproxy/dealloc())*