# prepareInterfaceForUserChoosingTextToInsert()

**Framework**: Authentication Services  
**Kind**: method

Prepare the view controller to show a list of all insertable text with user selectable fields.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
@MainActor
func prepareInterfaceForUserChoosingTextToInsert()
```

#### Discussion

This method is called by the system to prepare the extension’s view controller to present a list of any insertable text with selectable fields.

In order for your extension to be presented in the list of options for text insertion request, your extension needs to specify a true value for the Information Property List key `ProvidesTextToInsert` under the `ASCredentialProviderExtensionCapabilities` dictionary.

```None
Info.plist
├─ NSExtension
    ├─ NSExtensionAttributes
        ├─ ASCredentialProviderExtensionCapabilities
            ├─ ProvidesTextToInsert => true
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderviewcontroller/prepareinterfaceforuserchoosingtexttoinsert())*