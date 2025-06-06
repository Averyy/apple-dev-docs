# perform(_:with:with:)

**Framework**: Objective-C Runtime  
**Kind**: method  
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

#### Return Value

An object that is the result of the message.

#### Discussion

This method is the same as [`perform(_:)`](nsobjectprotocol/perform(_:).md) except that you can supply two arguments for `aSelector`. `aSelector` should identify a method that can take two arguments of type id. For methods with other argument types and return values, use [`NSInvocation`](https://developer.apple.com/documentation/Foundation/NSInvocation).

## Parameters

- `aSelector`: A selector identifying the message to send. If   is  , an   is raised.
- `object1`: An object that is the first argument of the message.
- `object2`: An object that is the second argument of the message

## See Also

- [func method(for: Selector!) -> IMP!](nsobject-swift.class/method(for:).md)
  Locates and returns the address of the receiver’s implementation of a method so it can be called as a function.
- [func perform(Selector!) -> Unmanaged<AnyObject>!](nsobjectprotocol/perform(_:).md)
  Sends a specified message to the receiver and returns the result of the message.
- [func perform(Selector!, with: Any!) -> Unmanaged<AnyObject>!](nsobjectprotocol/perform(_:with:).md)
  Sends a message to the receiver with an object as the argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobjectprotocol/perform(_:with:with:))*