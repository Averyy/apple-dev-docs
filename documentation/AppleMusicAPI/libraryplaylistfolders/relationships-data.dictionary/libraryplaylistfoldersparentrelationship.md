# LibraryPlaylistFolders.Relationships.LibraryPlaylistFoldersParentRelationship

**Framework**: Apple Music API  
**Kind**: dictionary

A resource object that represents the parent relationship of a library playlist folder.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object LibraryPlaylistFolders.Relationships.LibraryPlaylistFoldersParentRelationship
```

## Properties

- `href` (string): The relative location for the parent relationship.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the relationship if more exist.
- `data` ([LibraryPlaylistFolders]) *(required)*: The parent of the library playlist, if it exists.

## See Also

- [object LibraryPlaylistFolders.Relationships.LibraryPlaylistFoldersChildrenRelationship](libraryplaylistfolders/relationships-data.dictionary/libraryplaylistfolderschildrenrelationship.md)
  A resource object that represents the children relationship of a library playlist folder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/libraryplaylistfolders/relationships-data.dictionary/libraryplaylistfoldersparentrelationship)*