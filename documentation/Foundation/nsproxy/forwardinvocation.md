# forwardInvocation(_:)

**Framework**: Foundation  
**Kind**: method

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

#### Discussion

`NSProxy`’s implementation merely raises `NSInvalidArgumentException`. Override this method in your subclass to handle `invocation` appropriately, at the very least by setting its return value.

For example, if your proxy merely forwards messages to an instance variable named `realObject`, it can implement [`forwardInvocation(_:)`](nsproxy/forwardinvocation(_:).md) like this:

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsproxy/forwardinvocation(_:))*