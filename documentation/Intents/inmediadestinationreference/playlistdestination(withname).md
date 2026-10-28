# playlistDestination(withName:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates a new playlist destination for the media item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func playlistDestination(withName playlistName: String) -> Self
```

```objc
+ (instancetype) playlistDestinationWithName:(NSString *) playlistName;
```

## Return Value

A new [`INMediaDestinationReference`](../inmediadestinationreference.md) object or `nil` if unable to create.

## See Also

### Creating a Media Destination Object
- [class func library() -> Self](./library%28%29.md)
  Creates a new library destination for the media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediadestinationreference/playlistdestination(withname:))*