# init(query:)

**Framework**: Media Player  
**Kind**: init

Creates a new queue descriptor using the designated query.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(query: MPMediaQuery)
```

#### Return Value

A new queue descriptor consisting of the media items contained in the designated query.

#### Discussion

After creating a new queue descriptor, you can modify when individual media items start and stop playing, and which item in the queue plays first when playback begins.

## Parameters

- `query`: The query used to create the new queue descriptor.

## See Also

- [init(itemCollection: MPMediaItemCollection)](mpmusicplayermediaitemqueuedescriptor/init(itemcollection:).md)
  Creates a new queue descriptor using the designated collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayermediaitemqueuedescriptor/init(query:))*