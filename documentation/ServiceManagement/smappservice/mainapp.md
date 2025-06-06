# mainApp

**Framework**: Service Management  
**Kind**: property

An app service object that corresponds to the main application as a login item.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
class var mainApp: SMAppService { get }
```

#### Discussion

Use this `SMAppService` to configure the main app to launch at login.

## See Also

- [class func agent(plistName: String) -> Self](smappservice/agent(plistname:).md)
  Initializes an app service object with a launch agent with the property list name you provide.
- [class func daemon(plistName: String) -> Self](smappservice/daemon(plistname:).md)
  Initializes an app service object with a launch daemon with the property list name you provide.
- [class func loginItem(identifier: String) -> Self](smappservice/loginitem(identifier:).md)
  Initializes an app service object for a login item corresponding to the bundle with the identifier you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smappservice/mainapp)*