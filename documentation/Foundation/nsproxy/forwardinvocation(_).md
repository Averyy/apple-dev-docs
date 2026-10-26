# forwardInvocation(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Passes a given invocation to the real object the proxy represents.

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
func forwardInvocation(_ invocation: NSInvocation)
```

```objc
- (void) forwardInvocation:(NSInvocation *) invocation;
```

#### Discussion

`NSProxy`’s implementation merely raises `NSInvalidArgumentException`. Override this method in your subclass to handle `invocation` appropriately, at the very least by setting its return value.

For example, if your proxy merely forwards messages to an instance variable named `realObject`, it can implement [`forwardInvocation(_:)`](./forwardinvocation%28_%29.md) like this:

```objc
- (void)forwardInvocation:(NSInvocation *)anInvocation
{
    [anInvocation setTarget:realObject];
    [anInvocation invoke];
    return;
}
```

## Parameters

- `invocation`: The invocation to forward.

## See Also

### Handling Unimplemented Methods
- [- methodSignatureForSelector:](./methodsignatureforselector_.md)
  Raises `NSInvalidArgumentException`. Override this method in your concrete subclass to return a proper `NSMethodSignature` object for the given selector and the class your proxy objects stand in for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsproxy/forwardinvocation(_:))*