# forwardingTarget(for:)

**Framework**: Objective-C Runtime  
**Kind**: method

Returns the object to which unrecognized messages should first be directed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func forwardingTarget(for aSelector: Selector!) -> Any?
```

#### Return Value

The object to which unrecognized messages should first be directed.

#### Discussion

If an object implements (or inherits) this method, and returns a non-`nil` (and non-`self`) result, that returned object is used as the new receiver object and the message dispatch resumes to that new object. (Obviously if you return `self` from this method, the code would just fall into an infinite loop.)

If you implement this method in a non-root class, if your class has nothing to return for the given selector then you should return the result of invoking super’s implementation.

This method gives an object a chance to redirect an unknown message sent to it before the much more expensive [`forwardInvocation:`](nsobject-swift.class/forwardinvocation:.md) machinery takes over. This is useful when you simply want to redirect messages to another object and can be an order of magnitude faster than regular forwarding. It is not useful where the goal of the forwarding is to capture the NSInvocation, or manipulate the arguments or return value during the forwarding.

## Parameters

- `aSelector`: A   for a method that the receiver does not implement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/forwardingtarget(for:))*