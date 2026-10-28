# titleProperty(forGroupingType:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Type Method

Obtains the title key for a specified grouping type.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func titleProperty(forGroupingType groupingType: MPMediaGrouping) -> String
```

```objc
+ (NSString *) titlePropertyForGroupingType:(MPMediaGrouping) groupingType;
```

## Return Value

The title key for the group type.

## Discussion

Use this convenience method to obtain the key for the title that corresponds to a specified grouping type. For example, the following statement obtains the title key for the album grouping type:

**Swift**:

```swift
let titleIDKey = [MPMediaItem.persistentIDProperty(forGroupingType: MPMediaGrouping.album)]
```

**Objective-C**:

```objc
NSString *titleIDKey = [MPMediaItem titlePropertyForGroupingType: MPMediaGroupingAlbum];
```

You could then obtain the specific title that you want by using the [`value(forProperty:)`](../mpmediaentity/value%28forproperty%29.md) method. [`MPMediaGrouping`](../mpmediagrouping.md) describes grouping keys.

## Parameters

- `groupingType`: The grouping type that you want the title key for.

## See Also

### Obtaining group properties
- [class func persistentIDProperty(forGroupingType: MPMediaGrouping) -> String](./persistentidproperty%28forgroupingtype%29.md)
  Obtains the persistent identifier key for a specified grouping type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/titleproperty(forgroupingtype:))*