# prepare(forError:)

**Framework**: File Provider UI  
**Kind**: method  
**Role**: Instance Method

Performs any necessary setup or configuration when an authentication error occurs.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func prepare(forError error: any Error)
```

```objc
- (void) prepareForError:(NSError *) error;
```

#### Discussion

While your file provider is enumerating its content, the system calls this method whenever your file provider returns an [`NSFileProviderErrorDomain`](../../FileProvider/nsfileprovidererrordomain.md) error with a [`NSFileProviderError.Code.notAuthenticated`](../../FileProvider/nsfileprovidererror/code/notauthenticated.md) code. Use this method to present an interface to authenticate the user.

## Parameters

- `error`: An object representing the authentication error. Your File Provider extension can pass additional information in the error’s [`userInfo`](../../Foundation/nserror/userinfo.md) property.

## See Also

### Working with Actions
- [func prepare(forAction: String, itemIdentifiers: [NSFileProviderItemIdentifier])](./prepare%28foraction,itemidentifiers%29.md)
  Performs any necessary setup or configuration for the specified action.
- [var extensionContext: FPUIActionExtensionContext](./extensioncontext.md)
  The extension context provided by the host app.
- [class FPUIActionExtensionContext](../fpuiactionextensioncontext.md)
  An extension context provided to File Provider UI extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileproviderui/fpuiactionextensionviewcontroller/prepare(forerror:))*