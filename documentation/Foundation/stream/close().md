# close()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Closes the receiver.

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
func close()
```

```objc
- (void) close;
```

#### Discussion

Closing the stream terminates the flow of bytes and releases system resources that were reserved for the stream when it was opened. If the stream has been scheduled on a run loop, closing the stream implicitly removes the stream from the run loop. A stream that is closed can still be queried for its properties.

## See Also

### Using Streams
- [func open()](./open%28%29.md)
  Opens the receiving stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stream/close())*