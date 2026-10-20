# invokeUndefinedMethod(fromWebScript:withArguments:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Handles undefined method invocation from the scripting environment.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func invokeUndefinedMethod(fromWebScript name: String!, withArguments arguments: [Any]!) -> Any!
```

```objc
- (id) invokeUndefinedMethodFromWebScript:(NSString *) name withArguments:(NSArray *) arguments;
```

#### Return Value

The result of invoking the undefined method.

#### Discussion

This method is invoked when a script attempts to invoke a method not directly exported to the scripting environment. You should return the result of the invocation, converted appropriately for the scripting environment.

## Parameters

- `name`: The name of the undefined method.
- `arguments`: The arguments passed to the undefined method.

## See Also

### Invoking methods
- [func invokeDefaultMethod(withArguments: [Any]!) -> Any!](./invokedefaultmethod%28witharguments%29.md)
  Executes when a script attempts to invoke a method on an exposed object directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/invokeundefinedmethod(fromwebscript:witharguments:))*