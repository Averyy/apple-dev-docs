# invokeDefaultMethod(withArguments:)

**Framework**: Objective-C Runtime  
**Kind**: method

Executes when a script attempts to invoke a method on an exposed object directly.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func invokeDefaultMethod(withArguments arguments: [Any]!) -> Any!
```

#### Return Value

The result of invoking the default method.

## Parameters

- `arguments`: The arguments to be passed to the default method.

## See Also

- [func invokeUndefinedMethod(fromWebScript: String!, withArguments: [Any]!) -> Any!](nsobject-swift.class/invokeundefinedmethod(fromwebscript:witharguments:).md)
  Handles undefined method invocation from the scripting environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/invokedefaultmethod(witharguments:))*