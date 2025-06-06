# add(_:)

**Framework**: Group Activities  
**Kind**: method

Adds the specified item to the journal and begins transferring the item’s data to the other participants’ devices so they can access it.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
final func add<ItemType>(_ item: ItemType) async throws -> GroupSessionJournal.Attachment where ItemType : Transferable
```

#### Return Value

An attachment object you can remove by passing it to the [`remove(attachment:)`](groupsessionjournal/remove(attachment:).md) function.

#### Discussion

Call this method when you want to send a file or codable data type to the other participants of an activity. The method runs asynchronously and can return before the upload operation finishes.

## Parameters

- `item`: The item to send to other session participants. The type   you specify must conform to the    protocol. For more information about creating transferable types,   see  .

## See Also

- [func add<ItemType, MetadataType>(ItemType, metadata: MetadataType) async throws -> GroupSessionJournal.Attachment](groupsessionjournal/add(_:metadata:).md)
  Adds the specified item and metadata to the journal and begins transferring the data to the other participants’ devices so they can access it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionjournal/add(_:))*