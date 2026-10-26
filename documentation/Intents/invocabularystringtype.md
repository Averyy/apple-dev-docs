# INVocabularyStringType

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Possible usages for a custom vocabulary term.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum INVocabularyStringType
```

```c
enum INVocabularyStringType : NSInteger;
```

## Topics

### Constants
- [INVocabularyStringType.contactName](./invocabularystringtype/contactname.md)
  The name of an app-specific contact.
- [INVocabularyStringType.contactGroupName](./invocabularystringtype/contactgroupname.md)
  The name of a group of contacts, as a person would say it.
- [INVocabularyStringType.photoTag](./invocabularystringtype/phototag.md)
  A user-defined keyword associated with an image or images.
- [INVocabularyStringType.photoAlbumName](./invocabularystringtype/photoalbumname.md)
  The user-given name assigned to a collection of photographs.
- [INVocabularyStringType.workoutActivityName](./invocabularystringtype/workoutactivityname.md)
  The user-given name assigned to a workout.
- [INVocabularyStringType.carProfileName](./invocabularystringtype/carprofilename.md)
  The name of a vehicle configuration profile.
- [INVocabularyStringType.carName](./invocabularystringtype/carname.md)
  A name that identifies the user’s car.
- [INVocabularyStringType.paymentsOrganizationName](./invocabularystringtype/paymentsorganizationname.md)
  The name of the bank or company that holds the user’s account.
- [INVocabularyStringType.paymentsAccountNickname](./invocabularystringtype/paymentsaccountnickname.md)
  The user-given nickname for a bank account.
- [INVocabularyStringType.notebookItemTitle](./invocabularystringtype/notebookitemtitle.md)
  The title of a note, task, or task list.
- [INVocabularyStringType.notebookItemGroupName](./invocabularystringtype/notebookitemgroupname.md)
  The title of a group (or folder) containing the user’s notes or task lists.
- [INVocabularyStringType.mediaPlaylistTitle](./invocabularystringtype/mediaplaylisttitle.md)
  The name or title of a playlist.
- [INVocabularyStringType.mediaMusicArtistName](./invocabularystringtype/mediamusicartistname.md)
  The name of a musical artist.
- [INVocabularyStringType.mediaAudiobookTitle](./invocabularystringtype/mediaaudiobooktitle.md)
  The name or title of an audiobook.
- [INVocabularyStringType.mediaAudiobookAuthorName](./invocabularystringtype/mediaaudiobookauthorname.md)
  The name of an audiobook’s author.
- [INVocabularyStringType.mediaShowTitle](./invocabularystringtype/mediashowtitle.md)
  The name or title of a podcast or radio show.
### Initializers
- [init?(rawValue: Int)](./invocabularystringtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Updating the User-Specific Vocabulary
- [func setVocabulary(NSOrderedSet, of: INVocabularyStringType)](./invocabulary/setvocabulary%28_,of%29.md)
  Registers the specified vocabulary strings with the user.
- [func setVocabularyStrings(NSOrderedSet, of: INVocabularyStringType)](./invocabulary/setvocabularystrings%28_,of%29.md)
  Registers the specified vocabulary strings with the user.
- [func removeAllVocabularyStrings()](./invocabulary/removeallvocabularystrings%28%29.md)
  Removes all user-specific vocabulary strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/invocabularystringtype)*