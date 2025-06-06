# executeAndReturnError(_:)

**Framework**: Foundation  
**Kind**: method

Executes the receiver, compiling it first if it is not already compiled.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func executeAndReturnError(_ errorInfo: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> NSAppleEventDescriptor
```

#### Return Value

The result of executing the event, or `nil` if an error occurs.

#### Discussion

Any changes to property values caused by executing the script do not persist.

## Parameters

- `errorInfo`: On return, if an error occurs, a pointer to an error information dictionary.

## See Also

- [func compileAndReturnError(AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool](nsapplescript/compileandreturnerror(_:).md)
  Compiles the receiver, if it is not already compiled.
- [func executeAppleEvent(NSAppleEventDescriptor, error: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> NSAppleEventDescriptor](nsapplescript/executeappleevent(_:error:).md)
  Executes an Apple event in the context of the receiver, as a means of allowing the application to invoke a handler in the script.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsapplescript/executeandreturnerror(_:))*