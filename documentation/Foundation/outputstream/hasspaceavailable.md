# hasSpaceAvailable

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A boolean value that indicates whether the receiver can be written to.

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
var hasSpaceAvailable: Bool { get }
```

```objc
@property (readonly) BOOL hasSpaceAvailable;
```

## Discussion

[`true`](../../Swift/true.md) if the receiver can be written to or if a write must be attempted in order to determine if space is available, [`false`](../../Swift/false.md) otherwise.

## See Also

### Using Streams
- [func write(UnsafePointer<UInt8>, maxLength: Int) -> Int](./write%28_,maxlength%29.md)
  Writes the contents of a provided data buffer to the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/outputstream/hasspaceavailable)*