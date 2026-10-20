# init(storeIDs:)

**Framework**: Media Player  
**Kind**: init  
**Role**: Initializer

Creates a new queue descriptor using the designated store identifiers.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(storeIDs: [String])
```

```objc
- (instancetype) initWithStoreIDs:(NSArray<NSString *> *) storeIDs;
```

#### Return Value

A new queue descriptor consisting of the media items identified by the designated store identifiers.

## Parameters

- `storeIDs`: An array of store identifiers used to populate the queue descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerstorequeuedescriptor/init(storeids:))*