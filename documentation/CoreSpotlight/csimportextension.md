# CSImportExtension

**Framework**: Core Spotlight  
**Kind**: class  
**Role**: Class

An object that provides searchable attributes for file types that the app supports.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class CSImportExtension
```

```objc
@interface CSImportExtension : NSObject
```

## Overview

To create a Spotlight File Import extension, add a target to your app using the Spotlight File Import extension template in Xcode. The template project contains a subclass of `CSImportExtension`. To index content on a user’s device, Core Spotlight loads your extension and invokes the [`update(_:forFileAt:)`](./csimportextension/update%28_,forfileat%29.md) method. Core Spotlight passes a [`CSSearchableItemAttributeSet`](./cssearchableitemattributeset.md) and URL of a file to the extension, and you set properties that are relevant for the file.

> ❗ **Important**: Spotlight File Import extensions don’t provide functionality in macOS. To make custom files available to Spotlight in macOS, create a Spotlight importer plugin. For more information, refer to [Spotlight Importer Programming Guide](https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MDImporters/MDImporters.html#//apple_ref/doc/uid/TP40001267).

Typically, your extension loads details about the file and uses that information to set properties of the attribute set. For example, if your app contains files that are notes the user creates, it does the following:

```swift
class NoteImporter: CSImportExtension {
    override func update(_ attributes: CSSearchableItemAttributeSet, forFileAt contentURL: URL) throws {
        // NoteDetails is an app-defined object that encapsulates a note.
        guard let note = NoteDetails.noteDetails(for: contentURL) else {
            throw NoteError.noteNotFound
        }
        attributes.title = note.title
        attributes.contentCreationDate = note.creationDate
        attributes.userCreated = NSNumber(booleanLiteral: true)
    }
}
```

> ❗ **Important**:  Core Spotlight indexes files in batches and may call [`update(_:forFileAt:)`](./csimportextension/update%28_,forfileat%29.md) simultaneously on multiple queues with different values of `contentURL`.

To specify the file types your app supports, set the value of [`CSSupportedContentTypes`](../BundleResources/information-property-list/nsextension/nsextensionattributes/cssupportedcontenttypes.md) in your extension’s `Info.plist` file to an array of file type identifiers. For more information about file type identifiers, see [Uniform Type Identifiers](../UniformTypeIdentifiers/UniformTypeIdentifiers.md). The app in the previous example configures the extension’s `Info.plist` as follows:

```swift
<key>NSExtension</key>
<dict>
    <key>NSExtensionPointIdentifier</key>
    <string>com.apple.spotlight.import</string>
    <key>NSExtensionPrincipalClass</key>
    <string>FileImporter</string>
    <key>NSExtensionAttributes</key>
    <dict>
        <key>CSSupportedContentTypes</key>
        <array>
            <string>com.example.mynoteapp.note</string>
        </array>
    </dict>
</dict>

```

## Topics

### Providing searchable attributes
- [func update(CSSearchableItemAttributeSet, forFileAt: URL) throws](./csimportextension/update%28_,forfileat%29.md)
  Provides searchable attributes for a file at the specified URL.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Spotlight app extensions
- [Regenerating your app’s indexes on demand](./regenerating-your-app-s-indexes-on-demand.md)
  Create an app extension to maintain your app’s indexes and regenerate them as needed.
- [class CSIndexExtensionRequestHandler](./csindexextensionrequesthandler.md)
  An interface that implements an index-maintenance app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csimportextension)*