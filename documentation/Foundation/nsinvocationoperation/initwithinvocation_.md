# initWithInvocation:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns an `NSInvocationOperation` object initialized with the specified invocation object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
- (instancetype) initWithInvocation:(NSInvocation *) inv;
```

## Return Value

An initialized `NSInvocationOperation` object or `nil` if the object could not be initialized.

## Discussion

This method is the designated initializer. The receiver tells the invocation object to retain its arguments.

## Parameters

- `inv`: The invocation object identifying the target object, selector, and parameter objects.

## See Also

### Initialization
- [- initWithTarget:selector:object:](./initwithtarget_selector_object_.md)
  Returns an `NSInvocationOperation` object initialized with the specified target and selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsinvocationoperation/initwithinvocation:)*