# IntentFile

**Framework**: App Intents  
**Kind**: struct

An interface for providing an app entity that represents an on-disk file or file-based resource.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct IntentFile
```

## Mentions

- [Adding parameters to an app intent](adding-parameters-to-an-app-intent.md)

#### Overview

Provide an intent file entity implementation to describe data you store in a file on disk or in memory by providing its associated name and uniform type identifier.

## Topics

### Creating a file
- [init(data: Data, filename: String, type: UTType?)](intentfile/init(data:filename:type:).md)
- [init(fileURL: URL, filename: String?, type: UTType?)](intentfile/init(fileurl:filename:type:).md)
### Getting the file information
- [var filename: String](intentfile/filename.md)
  The human-readable name of the file, which will be displayed to the user.
- [var fileURL: URL?](intentfile/fileurl.md)
  URL to the file on disk, if any. If the file isn’t stored on disk, access the contents using the `data` property.
- [var type: UTType?](intentfile/type.md)
  The uniform type identifier of the file. (i.e. “public.json”, “public.png”, or any custom type) More information about uniform type identifiers can be found in <CoreServices/UTCoreTypes.h>
- [var data: Data](intentfile/data.md)
  The contents of the file. If the file was created with a URL, accessing this property will memory map the file contents.
- [var removedOnCompletion: Bool](intentfile/removedoncompletion.md)
  Indicates whether the file should be automatically deleted from disk when the Shortcut is done running. `false` by default.
### Instance Properties
- [var availableContentTypes: [UTType]](intentfile/availablecontenttypes.md)
  Valid content types the `IntentFile` can possibly be converted to.
### Instance Methods
- [func data(contentType: UTType) async throws -> Data](intentfile/data(contenttype:).md)
  Requests an `IntentFile` representation as binary data of the requested content type if possible.
- [func file(contentType: UTType, destinationDirectory: URL?) async throws -> (fileURL: URL, openedInPlace: Bool)](intentfile/file(contenttype:destinationdirectory:).md)
  Requests an `IntentFile` representation as a file url.
- [func withFile<Result>(contentType: UTType, allowOpenInPlace: Bool, fileHandler: (URL, Bool) async throws -> Result) async throws -> Result](intentfile/withfile(contenttype:allowopeninplace:filehandler:).md)
  Requests an `IntentFile` representation as a file url.
### Type Aliases
- [IntentFile.Specification](intentfile/specification.md)
- [IntentFile.UnwrappedType](intentfile/unwrappedtype.md)
- [IntentFile.ValueType](intentfile/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: EmptyResolverSpecification<IntentFile>](intentfile/defaultresolverspecification.md)
### Enumerations
- [IntentFile.IntentFileError](intentfile/intentfileerror.md)
### Default Implementations
- [Decodable Implementations](intentfile/decodable-implementations.md)
- [Encodable Implementations](intentfile/encodable-implementations.md)
- [Equatable Implementations](intentfile/equatable-implementations.md)
- [Hashable Implementations](intentfile/hashable-implementations.md)
- [InstanceDisplayRepresentable Implementations](intentfile/instancedisplayrepresentable-implementations.md)
- [TypeDisplayRepresentable Implementations](intentfile/typedisplayrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/CustomLocalizedStringResourceConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [DisplayRepresentable](displayrepresentable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [InstanceDisplayRepresentable](instancedisplayrepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TypeDisplayRepresentable](typedisplayrepresentable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentfile)*