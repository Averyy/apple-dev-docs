# applicationWithProcessIdentifier:

**Framework**: Scripting Bridge  
**Kind**: method  
**Role**: Type Method

Returns the shared instance representing a target application specified by its process identifier.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```objc
+ (SBApplication *) applicationWithProcessIdentifier:(pid_t) pid;
```

## Return Value

An instance of an `SBApplication` subclass that represents the target application whose process identifier is `pid`. Returns `nil` if no such application can be found or if the application does not have a scripting interface.

## Discussion

You should avoid using this method unless you know nothing about a target application but its process ID. In most cases, it is better to use [`applicationWithBundleIdentifier:`](./applicationwithbundleidentifier_.md), which will dynamically locate the application’s path at runtime, or [`applicationWithURL:`](./applicationwithurl_.md), which is not dependent on the target application being open at the time the method is called.

## Parameters

- `pid`: The BSD process ID of a OSA-compliant application. Often you can get the process ID of a process using the [`processIdentifier`](../../Foundation/process/processidentifier.md) method of `NSTask`.

## See Also

### Related Documentation
- [init?(processIdentifier: pid_t)](./init%28processidentifier%29.md)
  Returns an instance of an `SBApplication` subclass that represents the target application identified by the given process identifier.
### Getting a Scriptable Application Instance
- [+ applicationWithBundleIdentifier:](./applicationwithbundleidentifier_.md)
  Returns the shared instance representing the target application specified by its bundle identifier.
- [+ applicationWithURL:](./applicationwithurl_.md)
  Returns the shared instance representing a target application specified by the given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbapplication/applicationwithprocessidentifier:)*