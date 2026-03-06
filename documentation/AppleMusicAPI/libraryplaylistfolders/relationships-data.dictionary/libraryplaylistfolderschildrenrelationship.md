# LibraryPlaylistFolders.Relationships.LibraryPlaylistFoldersChildrenRelationship

**Framework**: Apple Music API  
**Kind**: dictionary

A resource object that represents the children relationship of a library playlist folder.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object LibraryPlaylistFolders.Relationships.LibraryPlaylistFoldersChildrenRelationship
```

## Properties

- `href` (string): The relative location for the children relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([*]) *(required)*: The children of the library playlist, if any exist.

## See Also

- [object LibraryPlaylistFolders.Relationships.LibraryPlaylistFoldersParentRelationship](libraryplaylistfolders/relationships-data.dictionary/libraryplaylistfoldersparentrelationship.md)
  A resource object that represents the parent relationship of a library playlist folder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/libraryplaylistfolders/relationships-data.dictionary/libraryplaylistfolderschildrenrelationship)*