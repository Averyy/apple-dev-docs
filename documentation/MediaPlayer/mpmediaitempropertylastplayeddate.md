# MPMediaItemPropertyLastPlayedDate

**Framework**: Media Player  
**Kind**: var

The most recent calendar date on which the user played the media item.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
let MPMediaItemPropertyLastPlayedDate: String
```

#### Discussion

Value is an [`NSDate`](https://developer.apple.com/documentation/Foundation/NSDate) object.

## See Also

- [let MPMediaItemPropertySkipCount: String](mpmediaitempropertyskipcount.md)
  The number of times the user has skipped playing the item.
- [let MPMediaItemPropertyRating: String](mpmediaitempropertyrating.md)
  The user-specified rating of the object in the range `[0...5]`, where a value of 5 indicates the most favorable rating.
- [let MPMediaItemPropertyUserGrouping: String](mpmediaitempropertyusergrouping.md)
  Corresponds to the “Grouping” field in the Info tab in the Get Info dialog in iTunes.
- [let MPMediaItemPropertyBookmarkTime: String](mpmediaitempropertybookmarktime.md)
  The user’s place in the media item the most recent time it was played.
- [let MPMediaItemPropertyDateAdded: String](mpmediaitempropertydateadded.md)
  The date the media item was added to the user’s Media library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaitempropertylastplayeddate)*