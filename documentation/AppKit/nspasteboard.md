# NSPasteboard

**Framework**: AppKit  
**Kind**: class

An object that transfers data to and from the pasteboard server.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSPasteboard
```

## Mentions

- [Supporting Writing Tools via the pasteboard](supporting-writing-tools-via-the-pasteboard.md)

#### Overview

The pasteboard server is shared by all running apps. It contains data that the user has cut or copied, as well as other data that one application wants to transfer to another. [`NSPasteboard`](nspasteboard.md) objects are an application’s sole interface to the server and to all pasteboard operations.

An [`NSPasteboard`](nspasteboard.md) object is also used to transfer data between apps and service providers listed in each application’s Services menu. The drag pasteboard is used to transfer data that is being dragged by the user.

A pasteboard can contain multiple items. You can directly write or read any object that implements the [`NSPasteboardWriting`](nspasteboardwriting.md) or [`NSPasteboardReading`](nspasteboardreading.md) [`Protocol`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45) respectively. This allows you to write and read common items such as URLs, colors, images, strings, attributed strings, and sounds without an intermediary object. Your custom classes can also implement these protocols for use with the pasteboard.

Writing methods such as [`setData(_:forType:)`](nspasteboard/setdata(_:fortype:).md) provide a convenient means of writing to the first pasteboard item, without having to create the first pasteboard item. You can use code like this, for example:

```objc
[pboard clearContents];
[pboard setData:data forType:type];
```

The general pasteboard, available by way of the [`general`](nspasteboard/general.md) class method, automatically participates with the Universal Clipboard feature in macOS 10.12 and later and in iOS 10.0 and later. There is no macOS API for interacting with this feature.

## Topics

### Creating and releasing a pasteboard
- [class var general: NSPasteboard](nspasteboard/general.md)
  The shared pasteboard object to use for general content.
- [init(byFilteringData: Data, ofType: NSPasteboard.PasteboardType)](nspasteboard/init(byfilteringdata:oftype:).md)
  Creates a new pasteboard object that supplies the specified data in as many types as possible based on the available filter services.
- [init(byFilteringFile: String)](nspasteboard/init(byfilteringfile:).md)
  Creates a new pasteboard object that supplies the specified file in as many types as possible based on the available filter services.
- [init(byFilteringTypesInPasteboard: NSPasteboard)](nspasteboard/init(byfilteringtypesinpasteboard:).md)
  Creates a new pasteboard object that supplies the specified pasteboard data in as many types as possible based on the available filter services.
- [init(name: NSPasteboard.Name)](nspasteboard/init(name:).md)
  Returns the pasteboard with the specified name.
- [NSPasteboard.Name](nspasteboard/name-swift.struct.md)
  Constants that represent the standard pasteboard names.
- [class func withUniqueName() -> NSPasteboard](nspasteboard/withuniquename.md)
  Creates and returns a new pasteboard with a name that is guaranteed to be unique with respect to other pasteboards in the system.
- [func releaseGlobally()](nspasteboard/releaseglobally.md)
  Releases the receiver’s resources in the pasteboard server.
### Determining pasteboard access
- [var accessBehavior: NSPasteboard.AccessBehavior](nspasteboard/accessbehavior-9k4t4.md)
  The current pasteboard access behavior. The user can customize this behavior per-app in System Settings for any app that has triggered a pasteboard access alert in the past.
- [var accessBehavior: NSPasteboard.AccessBehavior](nspasteboard/accessbehavior-86972.md)
  The current pasteboard access behavior. The user can customize this behavior per-app in System Settings for any app that has triggered a pasteboard access alert in the past.
- [NSPasteboard.AccessBehavior](nspasteboard/accessbehavior-swift.enum.md)
  A value indicating pasteboard access behavior.
### Writing data
- [func clearContents() -> Int](nspasteboard/clearcontents.md)
  Clears the existing contents of the pasteboard.
- [func writeObjects([any NSPasteboardWriting]) -> Bool](nspasteboard/writeobjects(_:).md)
  Writes an array of objects to the receiver.
- [func setData(Data?, forType: NSPasteboard.PasteboardType) -> Bool](nspasteboard/setdata(_:fortype:).md)
  Sets the data as the representation for the specified type for the first item on the receiver.
- [func setPropertyList(Any, forType: NSPasteboard.PasteboardType) -> Bool](nspasteboard/setpropertylist(_:fortype:).md)
  Sets the given property list as the representation for the specified type for the first item on the receiver.
- [func setString(String, forType: NSPasteboard.PasteboardType) -> Bool](nspasteboard/setstring(_:fortype:).md)
  Sets the given string as the representation for the specified type for the first item on the receiver.
- [NSPasteboard.PasteboardType](nspasteboard/pasteboardtype.md)
  The supported pasteboard types.
### Reading data
- [func readObjects(forClasses: [AnyClass], options: [NSPasteboard.ReadingOptionKey : Any]?) -> [Any]?](nspasteboard/readobjects(forclasses:options:).md)
  Reads from the receiver objects that best match the specified array of classes.
- [NSPasteboard.ReadingOptionKey](nspasteboard/readingoptionkey.md)
  Options for reading pasteboard data.
- [NSPasteboard.ReadingOptions](nspasteboard/readingoptions.md)
  Options that specify how to interpret data on the pasteboard when initializing pasteboard data.
- [var pasteboardItems: [NSPasteboardItem]?](nspasteboard/pasteboarditems.md)
  An array that contains all the items held by the pasteboard.
- [func index(of: NSPasteboardItem) -> Int](nspasteboard/index(of:).md)
  Returns the index of the specified pasteboard item.
- [func data(forType: NSPasteboard.PasteboardType) -> Data?](nspasteboard/data(fortype:).md)
  Returns the data for the specified type from the first item in the receiver that contains the type.
- [func propertyList(forType: NSPasteboard.PasteboardType) -> Any?](nspasteboard/propertylist(fortype:).md)
  Returns the property list for the specified type from the first item in the receiver that contains the type.
- [func string(forType: NSPasteboard.PasteboardType) -> String?](nspasteboard/string(fortype:).md)
  Returns a concatenation of the strings for the specified type from all the items in the receiver that contain the type.
### Validating contents
- [func availableType(from: [NSPasteboard.PasteboardType]) -> NSPasteboard.PasteboardType?](nspasteboard/availabletype(from:).md)
  Scans the specified types for a type that the receiver supports.
- [func canReadItem(withDataConformingToTypes: [String]) -> Bool](nspasteboard/canreaditem(withdataconformingtotypes:).md)
  Returns a Boolean value that indicates whether the receiver contains any items that conform to the specified UTIs.
- [func canReadObject(forClasses: [AnyClass], options: [NSPasteboard.ReadingOptionKey : Any]?) -> Bool](nspasteboard/canreadobject(forclasses:options:).md)
  Returns a Boolean value that indicates whether the receiver contains any items that can be represented as an instance of any class in a given array.
- [var types: [NSPasteboard.PasteboardType]?](nspasteboard/types.md)
  An array of the receiver’s supported data types.
- [class func types(filterableTo: NSPasteboard.PasteboardType) -> [NSPasteboard.PasteboardType]](nspasteboard/types(filterableto:).md)
  Returns the data types that can be converted to the specified type using the available filter services.
### Detecting patterns and metadata in pasteboard items
- [func detectedPatterns(for: Set<PartialKeyPath<NSPasteboard.DetectedValues>>) async throws -> Set<PartialKeyPath<NSPasteboard.DetectedValues>>](nspasteboard/detectedpatterns(for:).md)
  Determines whether the first pasteboard item matches the specified patterns, without notifying the person using the app.
- [func detectedValues(for: Set<PartialKeyPath<NSPasteboard.DetectedValues>>) async throws -> NSPasteboard.DetectedValues](nspasteboard/detectedvalues(for:).md)
  Determines whether the first pasteboard item matches the specified patterns, reading the contents if it finds a match.
- [NSPasteboard.DetectedValues](nspasteboard/detectedvalues.md)
  A type that contains common types of data that the data detection system matches for a pasteboard.
- [func detectedMetadata(for: Set<PartialKeyPath<NSPasteboard.DetectedMetadata>>) async throws -> NSPasteboard.DetectedMetadata](nspasteboard/detectedmetadata(for:).md)
  Determines available metadata from the specified metadata types for the first pasteboard item, without notifying the person using the app.
- [NSPasteboard.DetectedMetadata](nspasteboard/detectedmetadata.md)
  An object that contains common types of metadata that the data detection system matches for a pasteboard.
### Preparing the pasteboard for content
- [func prepareForNewContents(with: NSPasteboard.ContentsOptions) -> Int](nspasteboard/preparefornewcontents(with:).md)
  Prepares the pasteboard to receive new contents, removing the existing pasteboard contents.
- [NSPasteboard.ContentsOptions](nspasteboard/contentsoptions.md)
  Options for preparing the pasteboard.
### Getting information about a pasteboard
- [var name: NSPasteboard.Name](nspasteboard/name-swift.property.md)
  The receiver’s name.
- [var changeCount: Int](nspasteboard/changecount.md)
  The receiver’s change count.
### Writing data (macOS 10.5 and earlier)
- [func declareTypes([NSPasteboard.PasteboardType], owner: Any?) -> Int](nspasteboard/declaretypes(_:owner:).md)
  Prepares the receiver for a change in its contents by declaring the new types of data it will contain and a new owner.
- [func addTypes([NSPasteboard.PasteboardType], owner: Any?) -> Int](nspasteboard/addtypes(_:owner:).md)
  Adds promises for the specified types to the first pasteboard item.
- [func writeFileContents(String) -> Bool](nspasteboard/writefilecontents(_:).md)
  Writes the contents of the specified file to the pasteboard.
- [func write(FileWrapper) -> Bool](nspasteboard/write(_:).md)
  Writes the serialized contents of the specified file wrapper to the pasteboard.
### Reading data (macOS 10.5 and earlier)
- [func readFileContentsType(NSPasteboard.PasteboardType?, toFile: String) -> String?](nspasteboard/readfilecontentstype(_:tofile:).md)
  Reads data representing a file’s contents from the receiver and writes it to the specified file.
- [func readFileWrapper() -> FileWrapper?](nspasteboard/readfilewrapper.md)
  Reads data representing a file’s contents from the receiver and returns it as a file wrapper.
### Structures
- [NSPasteboard.WritingOptions](nspasteboard/writingoptions.md)
  Type to specify options for writing to a pasteboard.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSPasteboardItem](nspasteboarditem.md)
  An item on a pasteboard.
- [protocol NSPasteboardReading](nspasteboardreading.md)
  A set of methods that defines the interface for initializing an object from a pasteboard.
- [protocol NSPasteboardWriting](nspasteboardwriting.md)
  A set of methods that defines the interface for retrieving a representation of an object that can be written to a pasteboard.
- [protocol NSPasteboardItemDataProvider](nspasteboarditemdataprovider.md)
  A set of methods implemented by the data provider of a pasteboard item to provide the data for a particular UTI type.
- [NSPasteboard.ContentsOptions](nspasteboard/contentsoptions.md)
  Options for preparing the pasteboard.
- [protocol NSPasteboardTypeOwner](nspasteboardtypeowner.md)
  An object that serves as a data provider for data types that use lazy data fulfillment from a pasteboard request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard)*