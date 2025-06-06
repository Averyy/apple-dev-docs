# compileAndReturnError(_:)

**Framework**: Foundation  
**Kind**: method

Compiles the receiver, if it is not already compiled.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func compileAndReturnError(_ errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) for success or if the script was already compiled, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

## Parameters

- `errorInfo`: On return, if an error occurs, a pointer to an error information dictionary.

## See Also

- [func executeAndReturnError(AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> NSAppleEventDescriptor](nsapplescript/executeandreturnerror(_:).md)
  Executes the receiver, compiling it first if it is not already compiled.
- [func executeAppleEvent(NSAppleEventDescriptor, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> NSAppleEventDescriptor](nsapplescript/executeappleevent(_:error:).md)
  Executes an Apple event in the context of the receiver, as a means of allowing the application to invoke a handler in the script.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsapplescript/compileandreturnerror(_:))*