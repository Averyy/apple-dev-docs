# MPMediaItemPropertyUserGrouping

**Framework**: Media Player  
**Kind**: var  
**Role**: Global Variable

Corresponds to the “Grouping” field in the Info tab in the Get Info dialog in iTunes.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
let MPMediaItemPropertyUserGrouping: String
```

```c
extern NSString * const MPMediaItemPropertyUserGrouping;
```

#### Discussion

Value is an [`NSString`](../Foundation/nsstring.md) object.

## See Also

### User-defined property keys
- [let MPMediaItemPropertySkipCount: String](./mpmediaitempropertyskipcount.md)
  The number of times the user has skipped playing the item.
- [let MPMediaItemPropertyRating: String](./mpmediaitempropertyrating.md)
  The user-specified rating of the object in the range `[0...5]`, where a value of 5 indicates the most favorable rating.
- [let MPMediaItemPropertyLastPlayedDate: String](./mpmediaitempropertylastplayeddate.md)
  The most recent calendar date on which the user played the media item.
- [let MPMediaItemPropertyBookmarkTime: String](./mpmediaitempropertybookmarktime.md)
  The user’s place in the media item the most recent time it was played.
- [let MPMediaItemPropertyDateAdded: String](./mpmediaitempropertydateadded.md)
  The date the media item was added to the user’s Media library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaitempropertyusergrouping)*