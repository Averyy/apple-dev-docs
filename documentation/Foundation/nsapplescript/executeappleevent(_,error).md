# executeAppleEvent(_:error:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Executes an Apple event in the context of the receiver, as a means of allowing the application to invoke a handler in the script.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func executeAppleEvent(_ event: NSAppleEventDescriptor, error errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> NSAppleEventDescriptor
```

```objc
- (NSAppleEventDescriptor *) executeAppleEvent:(NSAppleEventDescriptor *) event error:(NSDictionary<NSString *,id> **) errorInfo;
```

## Return Value

The result of executing the event, or `nil` if an error occurs.

## Discussion

Compiles the receiver before executing it if it is not already compiled.

> ❗ **Important**:  You cannot use this method to send Apple events to other applications.

## Parameters

- `event`: The Apple event to execute.
- `errorInfo`: On return, if an error occurs, a pointer to an error information dictionary.

## See Also

### Compiling and Executing a Script
- [func compileAndReturnError(AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool](./compileandreturnerror%28_%29.md)
  Compiles the receiver, if it is not already compiled.
- [func executeAndReturnError(AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> NSAppleEventDescriptor](./executeandreturnerror%28_%29.md)
  Executes the receiver, compiling it first if it is not already compiled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsapplescript/executeappleevent(_:error:))*