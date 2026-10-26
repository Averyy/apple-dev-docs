# INVocabularyStringType.contactName

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The name of an app-specific contact.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case contactName
```

```c
INVocabularyStringTypeContactName
```

#### Discussion

For example, you might include the strings “Jon Smith” or “Apple Inc”. Don’t include names already in the Contacts app on the user’s device. Instead, use this type to define contacts that are exclusive to your app.

Siri puts your contact names in the [`nameComponents`](../inperson/namecomponents.md) or [`displayName`](../inperson/displayname.md) properties of any [`INPerson`](../inperson.md) object associated with intents related to calls, messages, payments, and photos.

## See Also

### Constants
- [INVocabularyStringType.contactGroupName](./contactgroupname.md)
  The name of a group of contacts, as a person would say it.
- [INVocabularyStringType.photoTag](./phototag.md)
  A user-defined keyword associated with an image or images.
- [INVocabularyStringType.photoAlbumName](./photoalbumname.md)
  The user-given name assigned to a collection of photographs.
- [INVocabularyStringType.workoutActivityName](./workoutactivityname.md)
  The user-given name assigned to a workout.
- [INVocabularyStringType.carProfileName](./carprofilename.md)
  The name of a vehicle configuration profile.
- [INVocabularyStringType.carName](./carname.md)
  A name that identifies the user’s car.
- [INVocabularyStringType.paymentsOrganizationName](./paymentsorganizationname.md)
  The name of the bank or company that holds the user’s account.
- [INVocabularyStringType.paymentsAccountNickname](./paymentsaccountnickname.md)
  The user-given nickname for a bank account.
- [INVocabularyStringType.notebookItemTitle](./notebookitemtitle.md)
  The title of a note, task, or task list.
- [INVocabularyStringType.notebookItemGroupName](./notebookitemgroupname.md)
  The title of a group (or folder) containing the user’s notes or task lists.
- [INVocabularyStringType.mediaPlaylistTitle](./mediaplaylisttitle.md)
  The name or title of a playlist.
- [INVocabularyStringType.mediaMusicArtistName](./mediamusicartistname.md)
  The name of a musical artist.
- [INVocabularyStringType.mediaAudiobookTitle](./mediaaudiobooktitle.md)
  The name or title of an audiobook.
- [INVocabularyStringType.mediaAudiobookAuthorName](./mediaaudiobookauthorname.md)
  The name of an audiobook’s author.
- [INVocabularyStringType.mediaShowTitle](./mediashowtitle.md)
  The name or title of a podcast or radio show.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/invocabularystringtype/contactname)*