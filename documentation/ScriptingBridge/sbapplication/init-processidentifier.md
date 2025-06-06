# init(processIdentifier:)

**Framework**: Scripting Bridge  
**Kind**: init

Returns an instance of an `SBApplication` subclass that represents the target application identified by the given process identifier.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
init?(processIdentifier pid: pid_t)
```

#### Return Value

An initialized `SBApplication` that you can use to communicate with the target application specified by the process ID. Returns `nil` if no such application can be found or if the application does not have a scripting interface.

#### Discussion

You should avoid using this method unless you know nothing about an external application but its PID. In most cases, it is better to use [`init(bundleIdentifier:)`](sbapplication/init(bundleidentifier:).md), which will dynamically locate the external application’s path at runtime, or [`init(url:)`](sbapplication/init(url:).md), which is not dependent on the external application being open at the time the method is called.

## Parameters

- `pid`: A BSD process ID specifying an application that is OSA-compliant.   Often you can get the process ID of a process using the     method of  .

## See Also

- [init?(bundleIdentifier: String)](sbapplication/init(bundleidentifier:).md)
  Returns an instance of an `SBApplication` subclass that represents the target application identified by the given bundle identifier.
- [init?(url: URL)](sbapplication/init(url:).md)
  Returns an instance of an `SBApplication` subclass that represents the target application identified by the given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbapplication/init(processidentifier:))*