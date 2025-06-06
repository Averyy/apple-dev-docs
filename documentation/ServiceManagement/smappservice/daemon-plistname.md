# daemon(plistName:)

**Framework**: Service Management  
**Kind**: method

Initializes an app service object with a launch daemon with the property list name you provide.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
class func daemon(plistName: String) -> Self
```

#### Return Value

An `SMService` object

#### Discussion

The property list name must correspond to a property list in the calling app’s `Contents/Library/LaunchDaemons` directory

## Parameters

- `plistName`: The name of the property list corresponding to the  .

## See Also

- [class var mainApp: SMAppService](smappservice/mainapp.md)
  An app service object that corresponds to the main application as a login item.
- [class func agent(plistName: String) -> Self](smappservice/agent(plistname:).md)
  Initializes an app service object with a launch agent with the property list name you provide.
- [class func loginItem(identifier: String) -> Self](smappservice/loginitem(identifier:).md)
  Initializes an app service object for a login item corresponding to the bundle with the identifier you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smappservice/daemon(plistname:))*