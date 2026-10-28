# methodSignatureForSelector:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Raises `NSInvalidArgumentException`. Override this method in your concrete subclass to return a proper `NSMethodSignature` object for the given selector and the class your proxy objects stand in for.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
- (NSMethodSignature *) methodSignatureForSelector:(SEL) sel;
```

## Return Value

Not applicable. The implementation provided by `NSProxy` raises an exception.

## Discussion

Be sure to avoid an infinite loop when necessary by checking that `sel` isn’t the selector for this method itself and by not sending any message that might invoke this method.

For example, if your proxy merely forwards messages to an instance variable named `realObject`, it can implement [`methodSignatureForSelector:`](./methodsignatureforselector_.md) like this:

```objc
– (NSMethodSignature *)methodSignatureForSelector:(SEL)aSelector
{
    return [realObject methodSignatureForSelector:aSelector];
}
```

## Parameters

- `sel`: The selector for which to return a method signature.

## See Also

### Related Documentation
- [- methodSignatureForSelector:](../../ObjectiveC/nsobject-swift.class/methodsignatureforselector_.md)
  Returns an `NSMethodSignature` object that contains a description of the method identified by a given selector.
### Handling Unimplemented Methods
- [func forwardInvocation(NSInvocation)](./forwardinvocation%28_%29.md)
  Passes a given invocation to the real object the proxy represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsproxy/methodsignatureforselector:)*