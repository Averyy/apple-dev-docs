# scriptErrorOffendingObjectDescriptor

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Sets a descriptor for an object that will be put in the reply Apple event if the sender requested a reply, execution of the receiver completes, and an error number was set.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var scriptErrorOffendingObjectDescriptor: NSAppleEventDescriptor? { get set }
```

```objc
@property (retain, nullable) NSAppleEventDescriptor * scriptErrorOffendingObjectDescriptor;
```

## Parameters

- `errorOffendingObjectDescriptor`: A descriptor that specifies an object that was responsible for an error.

## See Also

### Handling script execution errors
- [var scriptErrorExpectedTypeDescriptor: NSAppleEventDescriptor?](./scripterrorexpectedtypedescriptor.md)
  Sets a descriptor for the expected type that will be put in the reply Apple event if the sender requested a reply, execution of the receiver completes, and an error number was set.
- [var scriptErrorNumber: Int](./scripterrornumber.md)
  Sets a script error number that is associated with the execution of the command and is returned in the reply Apple event, if a reply was requested by the sender.
- [var scriptErrorString: String?](./scripterrorstring.md)
  Sets a script error string that is associated with execution of the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommand/scripterroroffendingobjectdescriptor)*