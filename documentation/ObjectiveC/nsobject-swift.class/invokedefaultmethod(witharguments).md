# invokeDefaultMethod(withArguments:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Executes when a script attempts to invoke a method on an exposed object directly.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func invokeDefaultMethod(withArguments arguments: [Any]!) -> Any!
```

```objc
- (id) invokeDefaultMethodWithArguments:(NSArray *) arguments;
```

#### Return Value

The result of invoking the default method.

## Parameters

- `arguments`: The arguments to be passed to the default method.

## See Also

### Invoking methods
- [func invokeUndefinedMethod(fromWebScript: String!, withArguments: [Any]!) -> Any!](./invokeundefinedmethod%28fromwebscript,witharguments%29.md)
  Handles undefined method invocation from the scripting environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/invokedefaultmethod(witharguments:))*