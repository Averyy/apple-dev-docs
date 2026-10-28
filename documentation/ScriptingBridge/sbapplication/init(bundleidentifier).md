# init(bundleIdentifier:)

**Framework**: Scripting Bridge  
**Kind**: init  
**Role**: Initializer

Returns an instance of an `SBApplication` subclass that represents the target application identified by the given bundle identifier.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
init?(bundleIdentifier ident: String)
```

```objc
- (SBApplication *) initWithBundleIdentifier:(NSString *) ident;
```

## Return Value

An initialized shared instance of an `SBApplication` subclass that represents a target application with the bundle identifier of `ident`. Returns `nil` if no such application can be found or if the application does not have a scripting interface.

## Discussion

If you must initialize an `SBApplication` object explictly, you should use this initializer if possible; unlike [`init(processIdentifier:)`](./init%28processidentifier%29.md) and [`init(url:)`](./init%28url%29-6xbe5.md), this method is not dependent on changeable factors such as the target application’s path or process ID. Even so, you should rarely have to initialize an `SBApplication` object yourself; instead, you should initialize an application-specific subclass such as `iTunesApplication`.

Note that this method does not check whether an application with the given bundle identifier actually exists.

## Parameters

- `ident`: A bundle identifier specifying an application that is OSA-compliant.

## See Also

### Initializing a Scriptable Application Object
- [init?(processIdentifier: pid_t)](./init%28processidentifier%29.md)
  Returns an instance of an `SBApplication` subclass that represents the target application identified by the given process identifier.
- [init?(url: URL)](./init%28url%29-6xbe5.md)
  Returns an instance of an `SBApplication` subclass that represents the target application identified by the given URL.
### Related Documentation
- [+ applicationWithBundleIdentifier:](./applicationwithbundleidentifier_.md)
  Returns the shared instance representing the target application specified by its bundle identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbapplication/init(bundleidentifier:))*