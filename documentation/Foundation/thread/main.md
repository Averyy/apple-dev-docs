# main

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Returns the `NSThread` object representing the main thread.

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
class var main: Thread { get }
```

```objc
@property (class, strong, readonly) NSThread * mainThread;
```

#### Return Value

The `NSThread` object representing the main thread.

## See Also

### Working with the Main Thread
- [class var isMainThread: Bool](./ismainthread-swift.type.property.md)
  Returns a Boolean value that indicates whether the current thread is the main thread.
- [var isMainThread: Bool](./ismainthread-swift.property.md)
  A Boolean value that indicates whether the receiver is the main thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/main)*