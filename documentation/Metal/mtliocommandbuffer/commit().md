# commit()

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Submits the command buffer to the queue for execution on the GPU.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func commit()
```

```objc
- (void) commit;
```

## Discussion

If you haven’t already called [`enqueue()`](./enqueue%28%29.md) for the command buffer, the [`commit()`](./commit%28%29.md) method enqueues it at the next position in the input/output command queue.

You can only commit an input/output command buffer once, after which you can’t encode any additional commands or add more completion handlers to it.

## See Also

### Submitting a command buffer
- [func enqueue()](./enqueue%28%29.md)
  Reserves a place for the input/output command buffer in the input/output command queue without committing the command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocommandbuffer/commit())*