# perform(_:with:with:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends a message to the receiver with two objects as arguments.

**Availability**:
- iOS 1.0+
- iPadOS 1.0+
- Mac Catalyst 1.0+
- macOS 10.0+
- tvOS 1.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func perform(_ aSelector: Selector!, with object1: Any!, with object2: Any!) -> Unmanaged<AnyObject>!
```

```objc
- (id) performSelector:(SEL) aSelector withObject:(id) object1 withObject:(id) object2;
```

## Return Value

An object that is the result of the message.

## Discussion

This method is the same as [`perform(_:)`](./perform%28_%29.md) except that you can supply two arguments for `aSelector`. `aSelector` should identify a method that can take two arguments of type id. For methods with other argument types and return values, use [`NSInvocation`](../../Foundation/nsinvocation.md).

## Parameters

- `aSelector`: A selector identifying the message to send. If `aSelector` is `NULL`, an [`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md) is raised.
- `object1`: An object that is the first argument of the message.
- `object2`: An object that is the second argument of the message

## See Also

### Related Documentation
- [func method(for: Selector!) -> IMP!](../nsobject-swift.class/method%28for%29.md)
  Locates and returns the address of the receiver’s implementation of a method so it can be called as a function.
### Sending Messages
- [func perform(Selector!) -> Unmanaged<AnyObject>!](./perform%28_%29.md)
  Sends a specified message to the receiver and returns the result of the message.
- [func perform(Selector!, with: Any!) -> Unmanaged<AnyObject>!](./perform%28_,with%29.md)
  Sends a message to the receiver with an object as the argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobjectprotocol/perform(_:with:with:))*