# initWithTarget:selector:object:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns an `NSInvocationOperation` object initialized with the specified target and selector.

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
- (instancetype) initWithTarget:(id) target selector:(SEL) sel object:(id) arg;
```

## Return Value

An initialized `NSInvocationOperation` object or `nil` if the target object does not implement the specified selector.

## Discussion

If you specify a selector with a non-void return type, you can get the return value by calling the [`result`](./result.md) method after the operation finishes executing. The receiver tells the invocation object to retain its arguments.

## Parameters

- `target`: The object defining the specified selector.
- `sel`: The selector to invoke when running the operation. The selector may take 0 or 1 parameters; if it accepts a parameter, the type of that parameter must be `id`. The return type of the method may be `void`, a scalar value, or an object that can be returned as an `id` type.
- `arg`: The parameter object to pass to the selector. If the selector does not take an argument, specify `nil`.

## See Also

### Related Documentation
- [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)
### Initialization
- [- initWithInvocation:](./initwithinvocation_.md)
  Returns an `NSInvocationOperation` object initialized with the specified invocation object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsinvocationoperation/initwithtarget:selector:object:)*