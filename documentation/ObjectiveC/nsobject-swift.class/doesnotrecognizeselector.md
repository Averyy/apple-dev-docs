# doesNotRecognizeSelector(_:)

**Framework**: Objective-C Runtime  
**Kind**: method

Handles messages the receiver doesn’t recognize.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func doesNotRecognizeSelector(_ aSelector: Selector!)
```

#### Discussion

The runtime system invokes this method whenever an object receives an `aSelector` message it can’t respond to or forward. This method, in turn, raises an `NSInvalidArgumentException`, and generates an error message.

Any [`doesNotRecognizeSelector(_:)`](nsobject-swift.class/doesnotrecognizeselector(_:).md) messages are generally sent only by the runtime system. However, they can be used in program code to prevent a method from being inherited. For example, an `NSObject` subclass might renounce the [`copy()`](nsobject-swift.class/copy().md) or [`init()`](nsobject-swift.class/init().md) method by re-implementing it to include a [`doesNotRecognizeSelector(_:)`](nsobject-swift.class/doesnotrecognizeselector(_:).md) message as follows:

```objc
- (id)copy
{
    [self doesNotRecognizeSelector:_cmd];
}
```

The `_cmd` variable is a hidden argument passed to every method that is the current selector; in this example, it identifies the selector for the `copy` method. This code prevents instances of the subclass from responding to `copy` messages or superclasses from forwarding `copy` messages—although [`responds(to:)`](nsobjectprotocol/responds(to:).md) will still report that the receiver has access to a `copy` method.

If you override this method, you must call `super` or raise an [`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException) exception at the end of your implementation. In other words, this method must not return normally; it must always result in an exception being thrown.

## Parameters

- `aSelector`: A   that identifies a method not implemented or recognized by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/doesnotrecognizeselector(_:))*