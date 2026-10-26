# mediaContainer

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The media item container.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
@NSCopying
var mediaContainer: INMediaItem? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INMediaItem * mediaContainer;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INMediaItem * mediaContainer;
```

#### Discussion

A container consists of one or more pieces of media content such as a playlist or album. You set [`mediaContainer`](./mediacontainer.md) when creating the [`INPlayMediaIntent`](../inplaymediaintent.md) object.

> **Note**:  This property isn’t used with SiriKit Intents.

## See Also

### Accessing Media Items
- [var mediaItems: [INMediaItem]?](./mediaitems.md)
  The media content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediaintent/mediacontainer)*