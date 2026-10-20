# compileAndReturnError(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Compiles the receiver, if it is not already compiled.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func compileAndReturnError(_ errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool
```

```objc
- (BOOL) compileAndReturnError:(NSDictionary<NSString *,id> **) errorInfo;
```

#### Return Value

[`true`](../../Swift/true.md) for success or if the script was already compiled, [`false`](../../Swift/false.md) otherwise.

## Parameters

- `errorInfo`: On return, if an error occurs, a pointer to an error information dictionary.

## See Also

### Compiling and Executing a Script
- [func executeAndReturnError(AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> NSAppleEventDescriptor](./executeandreturnerror%28_%29.md)
  Executes the receiver, compiling it first if it is not already compiled.
- [func executeAppleEvent(NSAppleEventDescriptor, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> NSAppleEventDescriptor](./executeappleevent%28_,error%29.md)
  Executes an Apple event in the context of the receiver, as a means of allowing the application to invoke a handler in the script.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsapplescript/compileandreturnerror(_:))*