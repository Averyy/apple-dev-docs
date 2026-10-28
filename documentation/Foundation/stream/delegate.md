# delegate

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Sets the receiver’s delegate.

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
unowned(unsafe) var delegate: (any StreamDelegate)? { get set }
```

```objc
@property (assign, nullable) id<NSStreamDelegate> delegate;
```

## Discussion

By default, a stream is its own delegate, and subclasses of `NSInputStream` and `NSOutputStream` must maintain this contract. If you override this method in a subclass, passing `nil` must restore the receiver as its own delegate. Delegates are not retained.

To learn about delegates and delegation, read “Delegation” in Cocoa Fundamentals Guide.

## Parameters

- `delegate`: The delegate for the receiver.

## See Also

### Configuring Streams
- [func property(forKey: Stream.PropertyKey) -> Any?](./property%28forkey%29.md)
  Returns the receiver’s property for a given key.
- [func setProperty(Any?, forKey: Stream.PropertyKey) -> Bool](./setproperty%28_,forkey%29.md)
  Attempts to set the value of a given property of the receiver and returns a Boolean value that indicates whether the value is accepted by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stream/delegate)*