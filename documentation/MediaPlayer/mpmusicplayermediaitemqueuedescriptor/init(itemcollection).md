# init(itemCollection:)

**Framework**: Media Player  
**Kind**: init  
**Role**: Initializer

Creates a new queue descriptor using the designated collection.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(itemCollection: MPMediaItemCollection)
```

```objc
- (instancetype) initWithItemCollection:(MPMediaItemCollection *) itemCollection;
```

#### Return Value

A new queue descriptor consisting of the media items contained in the designated collection.

#### Discussion

After creating a new queue descriptor, you can modify when individual media items start and stop playing, and which item in the queue plays first when playback begins.

## Parameters

- `itemCollection`: The collection of media items used to create the new queue descriptor.

## See Also

### Creating a new media item queue descriptor
- [init(query: MPMediaQuery)](./init%28query%29.md)
  Creates a new queue descriptor using the designated query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayermediaitemqueuedescriptor/init(itemcollection:))*