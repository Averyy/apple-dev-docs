# INVocabularyStringType.workoutActivityName

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The user-given name assigned to a workout.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case workoutActivityName
```

```c
INVocabularyStringTypeWorkoutActivityName
```

#### Discussion

For example, you might include the string “Half Marathon” or “Kettlebell exercise” for specific regimens created by the user.

Siri applies custom workout names to the [`workoutName`](../instartworkoutintent/workoutname.md) property of the [`INStartWorkoutIntent`](../instartworkoutintent.md), [`INPauseWorkoutIntent`](../inpauseworkoutintent.md), [`INResumeWorkoutIntent`](../inresumeworkoutintent.md), [`INEndWorkoutIntent`](../inendworkoutintent.md), and [`INCancelWorkoutIntent`](../incancelworkoutintent.md) classes.

## See Also

### Constants
- [INVocabularyStringType.contactName](./contactname.md)
  The name of an app-specific contact.
- [INVocabularyStringType.contactGroupName](./contactgroupname.md)
  The name of a group of contacts, as a person would say it.
- [INVocabularyStringType.photoTag](./phototag.md)
  A user-defined keyword associated with an image or images.
- [INVocabularyStringType.photoAlbumName](./photoalbumname.md)
  The user-given name assigned to a collection of photographs.
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

*[View on Apple Developer](https://developer.apple.com/documentation/intents/invocabularystringtype/workoutactivityname)*