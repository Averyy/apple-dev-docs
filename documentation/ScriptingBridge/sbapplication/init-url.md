# init(url:)

**Framework**: Scripting Bridge  
**Kind**: init

Returns an instance of an `SBApplication` subclass that represents the target application identified by the given URL.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
init?(url: URL)
```

#### Return Value

An initialized `SBApplication` that you can use to communicate with the target application specified by the process ID. Returns `nil` if an application could not be found or if the application does not have a scripting interface.

#### Discussion

This approach to initializing `SBApplication` objects should be used only if you know for certain the URL of the target application. In most cases, it is better to use [`applicationWithBundleIdentifier:`](sbapplication/applicationwithbundleidentifier:.md) which dynamically locates the target application at runtime. Even so, you should rarely have to initialize an `SBApplication` yourself.

This method currently supports file URLs (`file:`) and remote application URLs (`eppc:`). It checks whether a file exists at the specified path, but it does not check whether an application identified via `eppc:` exists.

## Parameters

- `url`: A Universal Resource Locator (URL) specifying an application that is   OSA-compliant.

## See Also

- [init?(bundleIdentifier: String)](sbapplication/init(bundleidentifier:).md)
  Returns an instance of an `SBApplication` subclass that represents the target application identified by the given bundle identifier.
- [init?(processIdentifier: pid_t)](sbapplication/init(processidentifier:).md)
  Returns an instance of an `SBApplication` subclass that represents the target application identified by the given process identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbapplication/init(url:))*