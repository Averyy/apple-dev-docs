# applicationWithBundleIdentifier:

**Framework**: Scripting Bridge  
**Kind**: method  
**Role**: Type Method

Returns the shared instance representing the target application specified by its bundle identifier.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```objc
+ (SBApplication *) applicationWithBundleIdentifier:(NSString *) ident;
```

#### Return Value

An instance of a `SBApplication` subclass that represents the target application whose bundle identifier is `ident`. Returns `nil` if no such application can be found or if the application does not have a scripting interface.

#### Discussion

For applications that declare themselves to have a dynamic scripting interface, this method will launch the application if it is not already running.

## Parameters

- `ident`: A bundle identifier specifying an application that is OSA-compliant.

## See Also

### Related Documentation
- [init?(bundleIdentifier: String)](./init%28bundleidentifier%29.md)
  Returns an instance of an `SBApplication` subclass that represents the target application identified by the given bundle identifier.
### Getting a Scriptable Application Instance
- [+ applicationWithProcessIdentifier:](./applicationwithprocessidentifier_.md)
  Returns the shared instance representing a target application specified by its process identifier.
- [+ applicationWithURL:](./applicationwithurl_.md)
  Returns the shared instance representing a target application specified by the given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbapplication/applicationwithbundleidentifier:)*