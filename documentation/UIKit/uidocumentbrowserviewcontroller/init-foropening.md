# init(forOpening:)

**Framework**: UIKit  
**Kind**: init

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

## Parameters

- `contentTypes`: An array of uniform type identifiers. If `nil`, the browser uses the document types that the [`CFBundleDocumentTypes`](https://developer.apple.com/documentation/bundleresources/information-property-list/cfbundledocumenttypes) key specifies in the app’s `Info.plist` file. For detailed instructions about setting the `CFBundleDocumentTypes` key, see [`Setting up a document browser app`](setting-up-a-document-browser-app.md). For more information about type identifiers, see [`Uniform Type Identifiers`](https://developer.apple.com/documentation/uniformtypeidentifiers).

## See Also

- [Adding a document browser to your app](adding-a-document-browser-to-your-app.md)
  Give people access to their local or remote documents from within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller/init(foropening:))*