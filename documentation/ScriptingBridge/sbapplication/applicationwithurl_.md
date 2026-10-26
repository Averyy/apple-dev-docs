# applicationWithURL:

**Framework**: Scripting Bridge  
**Kind**: method  
**Role**: Type Method

Returns the shared instance representing a target application specified by the given URL.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```objc
+ (SBApplication *) applicationWithURL:(NSURL *) url;
```

#### Return Value

An `SBApplication` subclass from which to generate a shared instance of the target application whose URL is `url`. Returns `nil` if no such application can be found or if the application does not have a scripting interface.

#### Discussion

For applications that declare themselves to have a dynamic scripting interface, this method will launch the application if it is not already running. This approach to initializing `SBApplication` objects should be used only if you know for certain the URL of the target application. In most cases, it is better to use [`applicationWithBundleIdentifier:`](./applicationwithbundleidentifier_.md) which dynamically locates the target application at runtime.

This method currently supports file URLs (`file:`) and remote application URLs (`eppc:`). It checks whether a file exists at the specified path, but it does not check whether an application identified via `eppc:` exists.

## Parameters

- `url`: The Universal Resource Locator (URL) locating an OSA-compliant application.

## See Also

### Related Documentation
- [init?(url: URL)](./init%28url%29-6xbe5.md)
  Returns an instance of an `SBApplication` subclass that represents the target application identified by the given URL.
### Getting a Scriptable Application Instance
- [+ applicationWithBundleIdentifier:](./applicationwithbundleidentifier_.md)
  Returns the shared instance representing the target application specified by its bundle identifier.
- [+ applicationWithProcessIdentifier:](./applicationwithprocessidentifier_.md)
  Returns the shared instance representing a target application specified by its process identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbapplication/applicationwithurl:)*