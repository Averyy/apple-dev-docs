# init(name:bundleIdentifier:)

**Framework**: InputMethodKit  
**Kind**: init

Creates and returns a server object from property list information contained in the provided bundle.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init!(name: String!, bundleIdentifier: String!)
```

#### Return Value

An initialized server object.

#### Discussion

This method examines the `Info.plist` file  for the entries shown in the table below. The class names are loaded, but no classes are instantiated. Additionally, an [`NSConnection`](https://developer.apple.com/documentation/Foundation/NSConnection) object is allocated and registered using the input method connection name supplied in the `Info.plist` file.

| Key | Value |
| --- | --- |
| `LSBackgroundOnly` | The associated value is `1`, because input methods are background-only applications. |
| `InputMethodConnectionName` | A string that specifies an input method connection name that names the connection through which your input method services are published. The Input Method Kit uses this name to create an `NSConnection` object through which clients deliver text input. |
| `InputMethodServerControllerClass` | An input controller class. |
| `tsInputMethodIconFileKey` | An icon file name. The icon is used to display your input method in the International pane of System Preferences. |
| `tsInputMethodCharacterRepertoireKey` | An array of one or more ISO language codes that specify the character repertoire of your input method. The codes help categorize your input method to the user. |

## Parameters

- `name`: The name to initialize the server object with.
- `bundleIdentifier`: The bundle identifier.

## See Also

- [init!(name: String!, controllerClass: AnyClass!, delegateClass: AnyClass!)](imkserver/init(name:controllerclass:delegateclass:).md)
  Creates and returns a server object initialized with the provided parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkserver/init(name:bundleidentifier:))*