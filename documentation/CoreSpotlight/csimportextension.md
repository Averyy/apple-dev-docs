# CSImportExtension

**Framework**: Core Spotlight  
**Kind**: class

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

#### Overview

To create a Spotlight File Importer extension, add a target to your app using the Spotlight File Importer template in Xcode. The template project contains a subclass of `CSImportExtension`. To index content on a user’s device, Core Spotlight loads your extension and invokes the [`update(_:forFileAt:)`](csimportextension/update(_:forfileat:).md) method. Core Spotlight passes a [`CSSearchableItemAttributeSet`](cssearchableitemattributeset.md) and URL of a file to the extension, and you set properties that are relevant for the file.

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

> ❗ **Important**:  Core Spotlight indexes files in batches and may call [`update(_:forFileAt:)`](csimportextension/update(_:forfileat:).md) simultaneously on multiple queues with different values of `contentURL`.

To specify the file types your app supports, set the value of [`CSSupportedContentTypes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSExtension/NSExtensionAttributes/CSSupportedContentTypes) in your extension’s `Info.plist` file to an array of file type identifiers. For more information about file type identifiers, see [`Uniform Type Identifiers`](https://developer.apple.com/documentation/UniformTypeIdentifiers). The app in the previous example configures the extension’s `Info.plist` as follows:

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
- [func update(CSSearchableItemAttributeSet, forFileAt: URL) throws](csimportextension/update(_:forfileat:).md)
  Provides searchable attributes for a file at the specified URL.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Regenerating your app’s indexes on demand](regenerating-your-app-s-indexes-on-demand.md)
  Create an app extension to maintain your app’s indexes and regenerate them as needed.
- [class CSIndexExtensionRequestHandler](csindexextensionrequesthandler.md)
  An interface that implements an index-maintenance app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csimportextension)*