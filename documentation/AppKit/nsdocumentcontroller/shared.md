# shared

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the shared `NSDocumentController` instance.

**Availability**:
- macOS

## Declaration

```swift
class var shared: NSDocumentController { get }
```

```objc
@property (class, strong, readonly) NSDocumentController * sharedDocumentController;
```

#### Return Value

The shared `NSDocumentController` instance.

#### Discussion

If an `NSDocumentController` instance doesn’t exist yet, it is created.

Initialization reads in the document types from the `CFBundleDocumentTypes` property list (in `Info.plist`), registers the instance for [`willPowerOffNotification`](../nsworkspace/willpoweroffnotification.md)s, and turns on the flag indicating that document user interfaces should be visible. You should always obtain your application’s `NSDocumentController` using this method.

## See Also

### Related Documentation
- [Developing a Document-Based App](../developing-a-document-based-app.md)
  Write an app that creates, manages, edits, and saves text documents.
- [- setShouldCreateUI:](./setshouldcreateui_.md)
  Sets whether the window controllers of a document should be created when the document is created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/shared)*