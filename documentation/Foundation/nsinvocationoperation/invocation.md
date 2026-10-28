# invocation

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The receiver’s invocation object.

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
@property (retain, readonly) NSInvocation * invocation;
```

## Discussion

The invocation object identifying the target object, selector, and parameters to use to execute the operation’s task.

## See Also

### Related Documentation
- [- initWithTarget:selector:object:](./initwithtarget_selector_object_.md)
  Returns an `NSInvocationOperation` object initialized with the specified target and selector.
- [- initWithInvocation:](./initwithinvocation_.md)
  Returns an `NSInvocationOperation` object initialized with the specified invocation object.
### Getting Attributes
- [result](./result.md)
  The result of the invocation or method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsinvocationoperation/invocation)*