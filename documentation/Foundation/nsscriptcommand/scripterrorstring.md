# scriptErrorString

**Framework**: Foundation  
**Kind**: property

Sets a script error string that is associated with execution of the command.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var scriptErrorString: String? { get set }
```

#### Discussion

If you override [`performDefaultImplementation()`](nsscriptcommand/performdefaultimplementation().md) and an error occurs, you should call this method to supply a string that provides a useful explanation. In fact, any script handler should call this method when an error occurs.

Calling this method alone does not cause an error message to be displayed—you must also call [`scriptErrorNumber`](nsscriptcommand/scripterrornumber.md) to supply an error number.

## Parameters

- `errorString`: A string that describes an error.

## See Also

- [var scriptErrorExpectedTypeDescriptor: NSAppleEventDescriptor?](nsscriptcommand/scripterrorexpectedtypedescriptor.md)
  Sets a descriptor for the expected type that will be put in the reply Apple event if the sender requested a reply, execution of the receiver completes, and an error number was set.
- [var scriptErrorNumber: Int](nsscriptcommand/scripterrornumber.md)
  Sets a script error number that is associated with the execution of the command and is returned in the reply Apple event, if a reply was requested by the sender.
- [var scriptErrorOffendingObjectDescriptor: NSAppleEventDescriptor?](nsscriptcommand/scripterroroffendingobjectdescriptor.md)
  Sets a descriptor for an object that will be put in the reply Apple event if the sender requested a reply, execution of the receiver completes, and an error number was set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommand/scripterrorstring)*