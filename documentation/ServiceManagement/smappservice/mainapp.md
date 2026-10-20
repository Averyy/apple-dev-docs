# mainApp

**Framework**: Service Management  
**Kind**: property  
**Role**: Type Property

An app service object that corresponds to the main application as a login item.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
class var mainApp: SMAppService { get }
```

```objc
@property (class, readonly) SMAppService * mainAppService;
```

#### Discussion

Use this `SMAppService` to configure the main app to launch at login.

## See Also

### Managing apps
- [class func agent(plistName: String) -> Self](./agent%28plistname%29.md)
  Initializes an app service object with a launch agent with the property list name you provide.
- [class func daemon(plistName: String) -> Self](./daemon%28plistname%29.md)
  Initializes an app service object with a launch daemon with the property list name you provide.
- [class func loginItem(identifier: String) -> Self](./loginitem%28identifier%29.md)
  Initializes an app service object for a login item corresponding to the bundle with the identifier you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smappservice/mainapp)*