# agent(plistName:)

**Framework**: Service Management  
**Kind**: method  
**Role**: Type Method

Initializes an app service object with a launch agent with the property list name you provide.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
class func agent(plistName: String) -> Self
```

```objc
+ (instancetype) agentServiceWithPlistName:(NSString *) plistName;
```

#### Discussion

The property list name must correspond to a property list in the calling app’s `Contents/Library/LaunchAgents` directory.

## Parameters

- `plistName`: The name of the property list corresponding to the [`SMAppService`](../smappservice.md).

## See Also

### Managing apps
- [class var mainApp: SMAppService](./mainapp.md)
  An app service object that corresponds to the main application as a login item.
- [class func daemon(plistName: String) -> Self](./daemon%28plistname%29.md)
  Initializes an app service object with a launch daemon with the property list name you provide.
- [class func loginItem(identifier: String) -> Self](./loginitem%28identifier%29.md)
  Initializes an app service object for a login item corresponding to the bundle with the identifier you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smappservice/agent(plistname:))*