# NSItemProvider

**Framework**: Foundation  
**Kind**: class

An item provider for conveying data or a file between processes during drag-and-drop or copy-and-paste activities, or from a host app to an app extension.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSItemProvider
```

#### Overview

Starting in iOS 11, item providers play a central role in drag and drop, and in copy and paste. They continue to play a role with app extensions.

The system uses an internal queue when calling the completion blocks for the `NSItemProvider` class. When using an item provider with drag and drop, ensure that UI updates take place on the main queue as follows:

```swift
DispatchQueue.main.async {
    // Work that impacts the user interface.
}
```

##### App Extension Support

An app extension typically encounters item providers when examining the [`attachments`](nsextensionitem/attachments.md) property of an [`NSExtensionItem`](nsextensionitem.md) object. During that examination, the extension can use the [`hasItemConformingToTypeIdentifier(_:)`](nsitemprovider/hasitemconformingtotypeidentifier(_:).md) method to look for data that it recognizes. Item providers use [`Uniform Type Identifiers`](https://developer.apple.com/documentation/UniformTypeIdentifiers) values to identify the data they contain. After finding a type of data that your extension can use, it calls the [`loadItem(forTypeIdentifier:options:completionHandler:)`](nsitemprovider/loaditem(fortypeidentifier:options:completionhandler:).md) method to load the actual data, which is delivered to the provided completion handler.

You can create item providers to vend data to another process. An extension that modifies an original data item can create a new `NSItemProvider` object to send back to the host app. When creating data items, you specify your data object and the type of that object. You can optionally use the [`previewImageHandler`](nsitemprovider/previewimagehandler.md) property to generate a preview image for your data.

A single item provider may use custom blocks to provide its data in many different formats. When configuring an item provider, use the [`registerItem(forTypeIdentifier:loadHandler:)`](nsitemprovider/registeritem(fortypeidentifier:loadhandler:).md) method to register your blocks and the formats each one supports. When a client requests data in a particular format, the item provider executes the corresponding block, which is then responsible for coercing the data to the appropriate type and returning it to the client.

## Topics

### Creating an item provider
- [convenience init?(contentsOf: URL!)](nsitemprovider/init(contentsof:).md)
  Provides data-backed content from an existing file.
- [convenience init(contentsOf: URL, contentType: UTType?, openInPlace: Bool, coordinated: Bool, visibility: NSItemProviderRepresentationVisibility)](nsitemprovider/init(contentsof:contenttype:openinplace:coordinated:visibility:).md)
  Provides data-backed content from an existing file with the specified parameters.
- [init(item: (any NSSecureCoding)?, typeIdentifier: String?)](nsitemprovider/init(item:typeidentifier:).md)
  Creates an item provider with an object, according to the item provider type coercion policy.
- [init()](nsitemprovider/init.md)
  Creates an empty item provider to which you can later register a data or file representation.
- [convenience init(object: any NSItemProviderWriting)](nsitemprovider/init(object:).md)
  Creates a new item provider, employing a specified object’s type identifiers to specify the data representations eligible for the provider to load.
### Configuring the provider
- [var preferredPresentationSize: CGSize](nsitemprovider/preferredpresentationsize.md)
  The ideal presentation size of the item.
- [var preferredPresentationStyle: NSItemProvider.PreferredPresentationStyle](nsitemprovider/preferredpresentationstyle-swift.property.md)
  The preferred style for presenting the item provider’s data.
- [NSItemProvider.PreferredPresentationStyle](nsitemprovider/preferredpresentationstyle-swift.enum.md)
  The presentation styles that determine how a view shows an item provider’s data.
- [var suggestedName: String?](nsitemprovider/suggestedname.md)
  The filename to use when writing the provided data to a file on disk.
- [var teamData: Data?](nsitemprovider/teamdata.md)
  The collection of data an app uses to hold private team information during drag and drop.
### Querying the provider’s contents
- [func canLoadObject(ofClass: any NSItemProviderReading.Type) -> Bool](nsitemprovider/canloadobject(ofclass:)-3eig9.md)
  Returns a Boolean value indicating whether an item provider can load objects of a specified class.
- [func canLoadObject<T>(ofClass: T.Type) -> Bool](nsitemprovider/canloadobject(ofclass:)-40grc.md)
  Returns a Boolean value indicating whether an item provider can load objects of a specified class.
- [func hasItemConformingToTypeIdentifier(String) -> Bool](nsitemprovider/hasitemconformingtotypeidentifier(_:).md)
  Returns a Boolean value indicating whether an item provider contains a data representation conforming to a specified universal type identifier file options parameter with a value of zero.
- [func hasRepresentationConforming(toTypeIdentifier: String, fileOptions: NSItemProviderFileOptions) -> Bool](nsitemprovider/hasrepresentationconforming(totypeidentifier:fileoptions:).md)
  Returns a Boolean value indicating whether an item provider contains a data representation conforming to a specified universal type identifier and to specified open-in-place behavior.
- [var registeredTypeIdentifiers: [String]](nsitemprovider/registeredtypeidentifiers.md)
  Returns the array of type identifiers for the item provider, in the same order they were registered.
- [func registeredTypeIdentifiers(fileOptions: NSItemProviderFileOptions) -> [String]](nsitemprovider/registeredtypeidentifiers(fileoptions:).md)
  Returns an array with a subset of type identifiers for the item provider, according to the specified file options, in the same order they were registered.
### Loading the provider’s contents
- [func loadItem(forTypeIdentifier: String, options: [AnyHashable : Any]?, completionHandler: NSItemProvider.CompletionHandler?)](nsitemprovider/loaditem(fortypeidentifier:options:completionhandler:).md)
  Loads the item’s data and coerces it to the specified type.
- [func loadDataRepresentation(forTypeIdentifier: String, completionHandler: (Data?, (any Error)?) -> Void) -> Progress](nsitemprovider/loaddatarepresentation(fortypeidentifier:completionhandler:).md)
  Asynchronously copies the provided, typed data into a generic data object, returning a progress object.
- [func loadDataRepresentation(for: UTType, completionHandler: (Data?, (any Error)?) -> Void) -> Progress](nsitemprovider/loaddatarepresentation(for:completionhandler:).md)
  Asynchronously copies the universal type data into a generic data object, returning a progress object.
- [func loadFileRepresentation(forTypeIdentifier: String, completionHandler: (URL?, (any Error)?) -> Void) -> Progress](nsitemprovider/loadfilerepresentation(fortypeidentifier:completionhandler:).md)
  Asynchronously writes a copy of the provided, typed data to a temporary file, returning a progress object.
- [func loadFileRepresentation(for: UTType, openInPlace: Bool, completionHandler: (URL?, Bool, (any Error)?) -> Void) -> Progress](nsitemprovider/loadfilerepresentation(for:openinplace:completionhandler:).md)
  Asynchronously writes a copy of the universal type data to a temporary file, returning a progress object.
- [func loadInPlaceFileRepresentation(forTypeIdentifier: String, completionHandler: (URL?, Bool, (any Error)?) -> Void) -> Progress](nsitemprovider/loadinplacefilerepresentation(fortypeidentifier:completionhandler:).md)
  Asynchronously opens a file in place, if possible, returning a progress object.
- [func loadObject(ofClass: any NSItemProviderReading.Type, completionHandler: ((any NSItemProviderReading)?, (any Error)?) -> Void) -> Progress](nsitemprovider/loadobject(ofclass:completionhandler:)-8ak5d.md)
  Asynchronously loads an object of a specified class to an item provider, returning a progress object.
- [func loadObject<T>(ofClass: T.Type, completionHandler: (T?, (any Error)?) -> Void) -> Progress](nsitemprovider/loadobject(ofclass:completionhandler:)-6pysm.md)
  Asynchronously loads an object of a specified class to an item provider, returning a progress object.
- [func loadTransferable<T>(type: T.Type, completionHandler: (Result<T, any Error>) -> Void) -> Progress](nsitemprovider/loadtransferable(type:completionhandler:).md)
  Asynchronously loads an object of a specified transferable type to an item provider, returning a progress object.
### Loading a preview image
- [func loadPreviewImage(options: [AnyHashable : Any]!, completionHandler: NSItemProvider.CompletionHandler!)](nsitemprovider/loadpreviewimage(options:completionhandler:).md)
  Loads the preview image for the item that the item provider represents.
- [var previewImageHandler: NSItemProvider.LoadHandler?](nsitemprovider/previewimagehandler.md)
  The custom preview image handler block for the item provider.
### Registering CloudKit shares
- [func registerCloudKitShare(CKShare, container: CKContainer)](nsitemprovider/registercloudkitshare(_:container:).md)
  Registers a CloudKit share for the user to modify.
- [func registerCloudKitShare(preparationHandler: ((CKShare?, CKContainer?, (any Error)?) -> Void) -> Void)](nsitemprovider/registercloudkitshare(preparationhandler:).md)
  Registers a handler that prepares a new CloudKit share.
- [func registerCKShare(CKShare, container: CKContainer, allowedSharingOptions: CKAllowedSharingOptions)](nsitemprovider/registerckshare(_:container:allowedsharingoptions:).md)
  Registers an existing collaboration object on a server.
- [func registerCKShare(container: CKContainer, allowedSharingOptions: CKAllowedSharingOptions, preparationHandler: () async throws -> CKShare)](nsitemprovider/registerckshare(container:allowedsharingoptions:preparationhandler:).md)
  Creates and registers a new collaboration object using a collection of records to share.
### Registering content types
- [var registeredContentTypes: [UTType]](nsitemprovider/registeredcontenttypes.md)
  Registered content types in the order the app registers each type.
- [var registeredContentTypesForOpenInPlace: [UTType]](nsitemprovider/registeredcontenttypesforopeninplace.md)
  Registered content types that the system can load as open-in-place files.
- [func registeredContentTypes(conformingTo: UTType) -> [UTType]](nsitemprovider/registeredcontenttypes(conformingto:).md)
  Returns an array of registered content types that conform to a specified content type.
### Registering data
- [func registerDataRepresentation(forTypeIdentifier: String, visibility: NSItemProviderRepresentationVisibility, loadHandler: ((Data?, (any Error)?) -> Void) -> Progress?)](nsitemprovider/registerdatarepresentation(fortypeidentifier:visibility:loadhandler:).md)
  Registers a data-backed representation for an item, specifiying item visibility and a load handler.
- [func registerDataRepresentation(for: UTType, visibility: NSItemProviderRepresentationVisibility, loadHandler: ((Data?, (any Error)?) -> Void) -> Progress?)](nsitemprovider/registerdatarepresentation(for:visibility:loadhandler:).md)
  Registers a data-backed representation for an item, specifiying item visibility and a load handler.
- [func registerItem(forTypeIdentifier: String, loadHandler: NSItemProvider.LoadHandler)](nsitemprovider/registeritem(fortypeidentifier:loadhandler:).md)
  Lazily registers an item, according to the item provider type coercion policy.
### Registering files
- [func registerFileRepresentation(forTypeIdentifier: String, fileOptions: NSItemProviderFileOptions, visibility: NSItemProviderRepresentationVisibility, loadHandler: ((URL?, Bool, (any Error)?) -> Void) -> Progress?)](nsitemprovider/registerfilerepresentation(fortypeidentifier:fileoptions:visibility:loadhandler:).md)
  Registers a file-backed representation for an item, specifying file options, item visibility, and a load handler.
- [func registerFileRepresentation(for: UTType, visibility: NSItemProviderRepresentationVisibility, openInPlace: Bool, loadHandler: ((URL?, Bool, (any Error)?) -> Void) -> Progress?)](nsitemprovider/registerfilerepresentation(for:visibility:openinplace:loadhandler:).md)
  Registers a file-backed representation for an item with item visibility, an open-in-place option, and a load handler.
### Registering group activities
- [func registerGroupActivity<ActivityType>(ActivityType)](nsitemprovider/registergroupactivity(_:).md)
  Registers a group activity instance with the specificed options.
- [func registerGroupActivity<ActivityType>(preparationHandler: () async throws -> ActivityType)](nsitemprovider/registergroupactivity(preparationhandler:).md)
  Registers a group activity instance asynchronously with the specified options.
### Registering objects
- [func registerObject(any NSItemProviderWriting, visibility: NSItemProviderRepresentationVisibility)](nsitemprovider/registerobject(_:visibility:).md)
  Adds representations of a specified object to an item provider, based on the object’s implementation of the item provider writing protocol, and adhering to a visibility specification.
- [func registerObject(ofClass: any NSItemProviderWriting.Type, visibility: NSItemProviderRepresentationVisibility, loadHandler: (((any NSItemProviderWriting)?, (any Error)?) -> Void) -> Progress?)](nsitemprovider/registerobject(ofclass:visibility:loadhandler:)-9sndn.md)
  Lazily adds representations of a specified object class to an item provider, based on the object’s implementation of the item provider writing protocol, and adhering to a visibility specification.
- [func registerObject<T>(ofClass: T.Type, visibility: NSItemProviderRepresentationVisibility, loadHandler: ((T?, (any Error)?) -> Void) -> Progress?)](nsitemprovider/registerobject(ofclass:visibility:loadhandler:)-133rx.md)
  Lazily adds representations of a specified object type to an item provider, based on the object’s implementation of the item provider writing protocol, and adhering to a visibility specification.
- [func register<T>(@autoclosure () -> T)](nsitemprovider/register(_:).md)
  Adds representations of a specified transferable type to an item provider.
### Getting the provider’s frame
- [var sourceFrame: NSRect](nsitemprovider/sourceframe.md)
  The rectangle that the item occupies in the host app’s source window.
- [var containerFrame: NSRect](nsitemprovider/containerframe.md)
  The rectangle of the item’s visible content.
### Constants
- [NSItemProvider.CompletionHandler](nsitemprovider/completionhandler.md)
  A block that receives the item provider’s data.
- [NSItemProvider.LoadHandler](nsitemprovider/loadhandler.md)
  A block that loads the item provider’s data and coerces it to the specified type.
- [Options Dictionary Key](options-dictionary-key.md)
  Keys indicating options to use when generating the item provider’s data.
- [Keys for Items Accessed in JavaScript Code](keys-for-items-accessed-in-javascript-code.md)
  Keys in property list items that the system recieves from or sends to JavaScript code.
- [class let errorDomain: String](nsitemprovider/errordomain.md)
  The error domain associated with the item provider.
- [struct NSItemProviderFileOptions](nsitemproviderfileoptions.md)
  Data-access specifications that declare how to handle items.
- [protocol NSItemProviderReading](nsitemproviderreading.md)
  The protocol for implementing a class to allow an item provider to create an instance of the class.
- [protocol NSItemProviderWriting](nsitemproviderwriting.md)
  The protocol for implementing a class to allow an item provider to retrieve data from an instance of the class.
- [enum NSItemProviderRepresentationVisibility](nsitemproviderrepresentationvisibility.md)
  Specifications that control which categories of processes can see an item.
- [NSItemProvider.ErrorCode](nsitemprovider/errorcode.md)
  The error codes that describe problems with consuming data from an item provider.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSExtensionItem](nsextensionitem.md)
  An immutable collection of values representing different aspects of an item for an extension to act upon.
- [Add Functionality to Finder with Action Extensions](../AppKit/add-functionality-to-finder-with-action-extensions.md)
  Implement Action Extensions to provide quick access to commonly used features of your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemprovider)*