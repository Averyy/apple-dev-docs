# finalize()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) finalize;
```

## Discussion

This method behaves as described in the `NSObject` class specification under the [`finalize()`](../../ObjectiveC/nsobject-swift.class/finalize%28%29.md) instance method. Note that a `finalize` method must be thread-safe.

## See Also

### Related Documentation
- [func dealloc()](./dealloc%28%29.md)
  Deallocates the memory occupied by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsproxy/finalize())*