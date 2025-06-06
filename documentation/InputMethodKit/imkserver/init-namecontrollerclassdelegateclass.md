# init(name:controllerClass:delegateClass:)

**Framework**: InputMethodKit  
**Kind**: init

Creates and returns a server object initialized with the provided parameters.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init!(name: String!, controllerClass controllerClassID: AnyClass!, delegateClass delegateClassID: AnyClass!)
```

#### Return Value

An initialized server object.

## Parameters

- `name`: The name to initialize the server object with.
- `controllerClassID`: The id for the input controller class.
- `delegateClassID`: The id for the delegate class.

## See Also

- [init!(name: String!, bundleIdentifier: String!)](imkserver/init(name:bundleidentifier:).md)
  Creates and returns a server object from property list information contained in the provided bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkserver/init(name:controllerclass:delegateclass:))*