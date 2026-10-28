# MPMediaItemPropertyRating

**Framework**: Media Player  
**Kind**: var  
**Role**: Global Variable

The user-specified rating of the object in the range `[0...5]`, where a value of 5 indicates the most favorable rating.

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
let MPMediaItemPropertyRating: String
```

```c
extern NSString * const MPMediaItemPropertyRating;
```

## Discussion

Value is an [`NSNumber`](../Foundation/nsnumber.md) object representing an [`NSUInteger`](../ObjectiveC/nsuinteger.md) data type.

## See Also

### User-defined property keys
- [let MPMediaItemPropertySkipCount: String](./mpmediaitempropertyskipcount.md)
  The number of times the user has skipped playing the item.
- [let MPMediaItemPropertyLastPlayedDate: String](./mpmediaitempropertylastplayeddate.md)
  The most recent calendar date on which the user played the media item.
- [let MPMediaItemPropertyUserGrouping: String](./mpmediaitempropertyusergrouping.md)
  Corresponds to the “Grouping” field in the Info tab in the Get Info dialog in iTunes.
- [let MPMediaItemPropertyBookmarkTime: String](./mpmediaitempropertybookmarktime.md)
  The user’s place in the media item the most recent time it was played.
- [let MPMediaItemPropertyDateAdded: String](./mpmediaitempropertydateadded.md)
  The date the media item was added to the user’s Media library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaitempropertyrating)*