# init(target:selector:object:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns an `NSThread` object initialized with the given arguments.

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
convenience init(target: Any, selector: Selector, object argument: Any?)
```

```objc
- (instancetype) initWithTarget:(id) target selector:(SEL) selector object:(id) argument;
```

#### Return Value

An `NSThread` object initialized with the given arguments.

#### Discussion

The objects `target` and `argument` are retained during the execution of the detached thread. They are released when the thread finally exits.

## Parameters

- `target`: The object to which the message specified by `selector` is sent.
- `selector`: The selector for the message to send to `target`. This selector must take only one argument and must not have a return value.
- `argument`: The single argument passed to the target. May be `nil`.

## See Also

### Related Documentation
- [func start()](./start%28%29.md)
  Starts the receiver.
### Initializing an NSThread Object
- [init()](./init%28%29.md)
  Returns an initialized `NSThread` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/init(target:selector:object:))*