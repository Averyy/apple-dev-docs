# init(forOpening:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a document browser view controller that can open the specified file types.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
init(forOpening contentTypes: [UTType]?)
```

```objc
- (instancetype) initForOpeningContentTypes:(NSArray<UTType *> *) contentTypes;
```

## Parameters

- `contentTypes`: An array of uniform type identifiers. If `nil`, the browser uses the document types that the [`CFBundleDocumentTypes`](../../BundleResources/information-property-list/cfbundledocumenttypes.md) key specifies in the app’s `Info.plist` file.

  For detailed instructions about setting the `CFBundleDocumentTypes` key, see [Setting up a document browser app](../setting-up-a-document-browser-app.md).

  For more information about type identifiers, see [Uniform Type Identifiers](../../UniformTypeIdentifiers/UniformTypeIdentifiers.md).

## See Also

### Creating a document browser
- [Adding a document browser to your app](../adding-a-document-browser-to-your-app.md)
  Give people access to their local or remote documents from within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/init(foropening:))*