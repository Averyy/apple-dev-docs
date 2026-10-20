# isMainThread

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Returns a Boolean value that indicates whether the current thread is the main thread.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class var isMainThread: Bool { get }
```

```objc
@property (class, readonly) BOOL isMainThread;
```

#### Return Value

[`true`](../../Swift/true.md) if the current thread is the main thread, otherwise [`false`](../../Swift/false.md).

## See Also

### Working with the Main Thread
- [var isMainThread: Bool](./ismainthread-swift.property.md)
  A Boolean value that indicates whether the receiver is the main thread.
- [class var main: Thread](./main.md)
  Returns the `NSThread` object representing the main thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/ismainthread-swift.type.property)*