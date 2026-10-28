# NSPasteboardItem

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An item on a pasteboard.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class NSPasteboardItem
```

```objc
@interface NSPasteboardItem : NSObject
```

## Overview

There are three main uses for an [`NSPasteboardItem`](./nspasteboarditem.md) object:

- Providing data on the pasteboard.

You can create one or more pasteboard items, set data or data providers for types, and write them to the pasteboard.

- Customizing data already on the pasteboard.

As a delegate or subclass, you can retrieve the pasteboard items currently on the pasteboard, read the existing types and data, and set new data and data providers for types as necessary.

- Retrieving data from the pasteboard.

You can retrieve pasteboard items from the pasteboard and then read the data for types you’re interested in.

A pasteboard item can be associated with a single pasteboard. When you create an item, you can write it to any pasteboard. When you pass an item to a pasteboard in [`writeObjects(_:)`](./nspasteboard/writeobjects%28_%29.md), that item becomes bound to the pasteboard it writes to. When you retrieve items from a pasteboard using [`pasteboardItems`](./nspasteboard/pasteboarditems.md) or [`readObjects(forClasses:options:)`](./nspasteboard/readobjects%28forclasses,options%29.md), the returned items are associated with the messaged pasteboard. Passing an item that is already associated with a pasteboard into [`writeObjects(_:)`](./nspasteboard/writeobjects%28_%29.md) causes an exception.

Use pasteboard items during a single pasteboard interaction, rather than retaining and reusing them. A pasteboard item is only valid until the owner of the pasteboard changes.

> ❗ **Important**:  When a pasteboard item’s owner changes, it becomes stale and its methods return an empty array, `nil`, or [`false`](../Swift/false.md).

## Topics

### Getting types
- [var types: [NSPasteboard.PasteboardType]](./nspasteboarditem/types.md)
  An array of uniform type identifier strings of the data types that the receiver supports.
- [func availableType(from: [NSPasteboard.PasteboardType]) -> NSPasteboard.PasteboardType?](./nspasteboarditem/availabletype%28from%29.md)
  Returns from a given array of types the first type within the pasteboard item, according to the ordering of types.
### Setting the data provider
- [func setDataProvider(any NSPasteboardItemDataProvider, forTypes: [NSPasteboard.PasteboardType]) -> Bool](./nspasteboarditem/setdataprovider%28_,fortypes%29.md)
  Sets the data provider for the specified types.
### Setting values
- [func setData(Data, forType: NSPasteboard.PasteboardType) -> Bool](./nspasteboarditem/setdata%28_,fortype%29.md)
  Sets the value for a specified type as a data object.
- [func setString(String, forType: NSPasteboard.PasteboardType) -> Bool](./nspasteboarditem/setstring%28_,fortype%29.md)
  Sets the value for a specified type as a string.
- [func setPropertyList(Any, forType: NSPasteboard.PasteboardType) -> Bool](./nspasteboarditem/setpropertylist%28_,fortype%29.md)
  Sets the value for a specified type as a property list.
### Getting values
- [func data(forType: NSPasteboard.PasteboardType) -> Data?](./nspasteboarditem/data%28fortype%29.md)
  Returns the value for the specified type as a data object.
- [func string(forType: NSPasteboard.PasteboardType) -> String?](./nspasteboarditem/string%28fortype%29.md)
  Returns the value for the specified type as a string.
- [func propertyList(forType: NSPasteboard.PasteboardType) -> Any?](./nspasteboarditem/propertylist%28fortype%29.md)
  Returns the value for the specified type as a property list.
### Detecting patterns and metadata in pasteboard items
- [func detectedPatterns(for: Set<PartialKeyPath<NSPasteboardItem.DetectedValues>>) async throws -> Set<PartialKeyPath<NSPasteboardItem.DetectedValues>>](./nspasteboarditem/detectedpatterns%28for%29.md)
  Determines whether the pasteboard item matches the specified patterns, without notifying the person using the app.
- [func detectedValues(for: Set<PartialKeyPath<NSPasteboardItem.DetectedValues>>) async throws -> NSPasteboardItem.DetectedValues](./nspasteboarditem/detectedvalues%28for%29.md)
  Determines whether this pasteboard item matches the specified patterns, reading the contents if it finds a match.
- [NSPasteboardItem.DetectedValues](./nspasteboarditem/detectedvalues.md)
- [func detectedMetadata(for: Set<PartialKeyPath<NSPasteboardItem.DetectedMetadata>>) async throws -> NSPasteboardItem.DetectedMetadata](./nspasteboarditem/detectedmetadata%28for%29.md)
  Determines available metadata from the specified metadata types for this pasteboard item, without notifying the person using the app.
- [NSPasteboardItem.DetectedMetadata](./nspasteboarditem/detectedmetadata.md)
- [- detectPatternsForPatterns:completionHandler:](./nspasteboarditem/detectpatternsforpatterns_completionhandler_.md)
  Determines whether this pasteboard item matches the specified patterns, without notifying the person using the app.
- [- detectValuesForPatterns:completionHandler:](./nspasteboarditem/detectvaluesforpatterns_completionhandler_.md)
  Determines whether this pasteboard item matches the specified patterns, reading the contents if it finds a match.
- [- detectMetadataForTypes:completionHandler:](./nspasteboarditem/detectmetadatafortypes_completionhandler_.md)
  Determines available metadata from the specified metadata types for this pasteboard item, without notifying the person using the app.
### Initializers
- [init?(pasteboardPropertyList: Any, ofType: NSPasteboard.PasteboardType)](./nspasteboarditem/init%28pasteboardpropertylist,oftype%29.md)
### Instance Properties
- [var collaborationMetadata: SWCollaborationMetadata?](./nspasteboarditem/collaborationmetadata.md)
  A model object you use for conveying data during a collaboration.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSPasteboardReading](./nspasteboardreading.md)
- [NSPasteboardWriting](./nspasteboardwriting.md)

## See Also

### Pasteboard
- [class NSPasteboard](./nspasteboard.md)
  An object that transfers data to and from the pasteboard server.
- [protocol NSPasteboardReading](./nspasteboardreading.md)
  A set of methods that defines the interface for initializing an object from a pasteboard.
- [protocol NSPasteboardWriting](./nspasteboardwriting.md)
  A set of methods that defines the interface for retrieving a representation of an object that can be written to a pasteboard.
- [protocol NSPasteboardItemDataProvider](./nspasteboarditemdataprovider.md)
  A set of methods implemented by the data provider of a pasteboard item to provide the data for a particular UTI type.
- [NSPasteboard.ContentsOptions](./nspasteboard/contentsoptions.md)
  Options for preparing the pasteboard.
- [protocol NSPasteboardTypeOwner](./nspasteboardtypeowner.md)
  An object that serves as a data provider for data types that use lazy data fulfillment from a pasteboard request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboarditem)*