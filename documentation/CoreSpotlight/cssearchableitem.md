# CSSearchableItem

**Framework**: Core Spotlight  
**Kind**: class

The details of your app-specific content that someone might search for on their devices.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
class CSSearchableItem
```

## Mentions

- [Adding your app’s content to Spotlight indexes](adding-your-app-s-content-to-spotlight-indexes.md)
- [Enabling Apple Intelligence summarization and prioritization](enable-apple-intelligence-summaries.md)
- [Searching for information in your app](searching-for-information-in-your-app.md)

#### Overview

A `CSSearchableItem` uniquely identifies a part of your app’s content, and provides the metadata that Spotlight indexes and uses to find that content later. As part of indexing your app’s content, you create searchable items and fill them with details about your app’s content and where to find it. After indexing the content, you can then execute queries using the Core Spotlight APIs to find the items you indexed. People can also use the system’s Spotlight search interface to find your app’s content.

When you create or update content in your app, create a `CSSearchableItem` for that content if you want it to be searchable. A searchable item contains identification strings you use to locate that item in your content and a [`CSSearchableItemAttributeSet`](cssearchableitemattributeset.md) object with details about the item. For the metadata, you typically want to provide values for the [`title`](cssearchableitemattributeset/title.md), [`displayName`](cssearchableitemattributeset/displayname.md), and [`contentType`](cssearchableitemattributeset/contenttype.md) attributes at a minimum. If you’re indexing a file on disk, provide a value for the [`contentURL`](cssearchableitemattributeset/contenturl.md) attribute. Fill in as many other attributes as makes sense for the content you’re indexing.

After creating a searchable item, index it using a [`CSSearchableIndex`](cssearchableindex.md) object. As you update your app’s content, update your `CSSearchableItem` objects for that content and index them right away. If you delete content, similarly delete the searchable items from the index. Keeping your app’s indexes current ensures that searches return valid information. For more information on indexing your content, see [`Adding your app’s content to Spotlight indexes`](adding-your-app-s-content-to-spotlight-indexes.md).

## Topics

### Getting a searchable item
- [init(uniqueIdentifier: String?, domainIdentifier: String?, attributeSet: CSSearchableItemAttributeSet)](cssearchableitem/init(uniqueidentifier:domainidentifier:attributeset:).md)
  Returns a searchable item associated with the specified identifier, domain identifier, and attribute set.
### Setting attributes on a searchable item
- [var uniqueIdentifier: String](cssearchableitem/uniqueidentifier.md)
  The value that uniquely identifies the searchable item within your app.
- [var domainIdentifier: String?](cssearchableitem/domainidentifier.md)
  An optional identifier that represents the domain or owner of the item.
- [var attributeSet: CSSearchableItemAttributeSet](cssearchableitem/attributeset.md)
  The set of attributes that contain metadata associated with the item in a [`CSSearchableItemAttributeSet`](cssearchableitemattributeset.md) object.
- [var expirationDate: Date!](cssearchableitem/expirationdate.md)
  The date after which the searchable item should no longer exist.
- [var isUpdate: Bool](cssearchableitem/isupdate.md)
  A Boolean value that indicates whether to treat the item as an update instead of a new item.
### Continuing a search or activity
- [let CSSearchableItemActionType: String](cssearchableitemactiontype.md)
  Indicates that the activity type to continue is related to a searchable item.
- [let CSSearchableItemActivityIdentifier: String](cssearchableitemactivityidentifier.md)
  The key you use to access a searchable item in a user activity object.
- [let CSQueryContinuationActionType: String](csquerycontinuationactiontype.md)
  Indicates that the activity type to continue is a search or query.
- [let CSSearchQueryString: String](cssearchquerystring.md)
  Provides the key for the current query in the info dictionary of the user activity object.
### Comparing items
- [func compare(byRank: CSSearchableItem) -> ComparisonResult](cssearchableitem/compare(byrank:).md)
  Compares two items by rank and returns the result.
### Structures
- [CSSearchableItem.UpdateListenerOptions](cssearchableitem/updatelisteneroptions-swift.struct.md)
  The set of options that contain metadata-associated summarization and prioritization of a searchable item.
### Initializers
- [convenience init(appEntity: some IndexedEntity)](cssearchableitem/init(appentity:).md)
  Intializes a new searchable item with the relevant fields populated from the provided app entity.
- [convenience init<Entity>(appEntity: Entity, priority: Int)](cssearchableitem/init(appentity:priority:).md)
  Intializes a new searchable item with the relevant fields populated from the provided app entity.
### Instance Properties
- [var updateListenerOptions: CSSearchableItem.UpdateListenerOptions](cssearchableitem/updatelisteneroptions-swift.property.md)
### Instance Methods
- [func associateAppEntity(some IndexedEntity, priority: Int)](cssearchableitem/associateappentity(_:priority:).md)
  Associates an app entity with this searchable item.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class CSSearchableItemAttributeSet](cssearchableitemattributeset.md)
  The detailed metadata for a searchable item.
- [class CSCustomAttributeKey](cscustomattributekey.md)
  A key associated with a custom attribute for a searchable item.
- [class CSLocalizedString](cslocalizedstring.md)
  An object that displays localized text in search results related to your app.
- [class CSPerson](csperson.md)
  An object that represents a person in the context of search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitem)*