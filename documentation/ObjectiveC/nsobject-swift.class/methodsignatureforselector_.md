# methodSignatureForSelector:

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Returns an `NSMethodSignature` object that contains a description of the method identified by a given selector.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```objc
- (NSMethodSignature *) methodSignatureForSelector:(SEL) aSelector;
```

#### Return Value

An `NSMethodSignature` object that contains a description of the method identified by `aSelector`, or `nil` if the method can’t be found.

#### Discussion

This method is used in the implementation of protocols. This method is also used in situations where an `NSInvocation` object must be created, such as during message forwarding. If your object maintains a delegate or is capable of handling messages that it does not directly implement, you should override this method to return an appropriate method signature.

## Parameters

- `aSelector`: A [Selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48) that identifies the method for which to return the implementation address. When the receiver is an instance, `aSelector` should identify an instance method; when the receiver is a class, it should identify a class method.

## See Also

### Related Documentation
- [- forwardInvocation:](./forwardinvocation_.md)
  Overridden by subclasses to forward messages to other objects.
### Obtaining Information About Methods
- [func method(for: Selector!) -> IMP!](./method%28for%29.md)
  Locates and returns the address of the receiver’s implementation of a method so it can be called as a function.
- [class func instanceMethod(for: Selector!) -> IMP!](./instancemethod%28for%29.md)
  Locates and returns the address of the implementation of the instance method identified by a given selector.
- [+ instanceMethodSignatureForSelector:](./instancemethodsignatureforselector_.md)
  Returns an `NSMethodSignature` object that contains a description of the instance method identified by a given selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/methodsignatureforselector:)*