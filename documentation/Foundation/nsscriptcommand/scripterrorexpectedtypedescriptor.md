# scriptErrorExpectedTypeDescriptor

**Framework**: Foundation  
**Kind**: property

Sets a descriptor for the expected type that will be put in the reply Apple event if the sender requested a reply, execution of the receiver completes, and an error number was set.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var scriptErrorExpectedTypeDescriptor: NSAppleEventDescriptor? { get set }
```

## Parameters

- `errorExpectedTypeDescriptor`: A descriptor that specifies a type.

## See Also

- [var scriptErrorNumber: Int](nsscriptcommand/scripterrornumber.md)
  Sets a script error number that is associated with the execution of the command and is returned in the reply Apple event, if a reply was requested by the sender.
- [var scriptErrorOffendingObjectDescriptor: NSAppleEventDescriptor?](nsscriptcommand/scripterroroffendingobjectdescriptor.md)
  Sets a descriptor for an object that will be put in the reply Apple event if the sender requested a reply, execution of the receiver completes, and an error number was set.
- [var scriptErrorString: String?](nsscriptcommand/scripterrorstring.md)
  Sets a script error string that is associated with execution of the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommand/scripterrorexpectedtypedescriptor)*