# scriptErrorNumber

**Framework**: Foundation  
**Kind**: property

Sets a script error number that is associated with the execution of the command and is returned in the reply Apple event, if a reply was requested by the sender.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var scriptErrorNumber: Int { get set }
```

#### Discussion

If you override [`performDefaultImplementation()`](nsscriptcommand/performdefaultimplementation().md) and an error occurs, you should call this method to supply an appropriate error number. In fact, any script handler should call this method when an error occurs. The error number you supply is returned in the reply Apple event.

Invoking `setScriptErrorNumber:` causes an error message to be displayed. To associate a specific error message with the error number, you invoke [`scriptErrorString`](nsscriptcommand/scripterrorstring.md). This make sense, for example, when you set an error number that is specific to your application, or when you can supply a specific and useful error message to the user.

If `setScriptErrorNumber:` is invoked on an `NSScriptCommand` with multiple receivers, the command will stop sending command handling messages to more receivers.

## Parameters

- `errorNumber`: An error number to associate with the command.

## See Also

- [var scriptErrorExpectedTypeDescriptor: NSAppleEventDescriptor?](nsscriptcommand/scripterrorexpectedtypedescriptor.md)
  Sets a descriptor for the expected type that will be put in the reply Apple event if the sender requested a reply, execution of the receiver completes, and an error number was set.
- [var scriptErrorOffendingObjectDescriptor: NSAppleEventDescriptor?](nsscriptcommand/scripterroroffendingobjectdescriptor.md)
  Sets a descriptor for an object that will be put in the reply Apple event if the sender requested a reply, execution of the receiver completes, and an error number was set.
- [var scriptErrorString: String?](nsscriptcommand/scripterrorstring.md)
  Sets a script error string that is associated with execution of the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommand/scripterrornumber)*