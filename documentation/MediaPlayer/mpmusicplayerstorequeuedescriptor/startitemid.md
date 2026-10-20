# startItemID

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The item identified by the store identifier to play first.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var startItemID: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * startItemID;
```

#### Discussion

When this property isn’t set, the value is [`nil`](../../ObjectiveC/nil-227m0.md) and the first item in the queue is the first item to play.

## See Also

### Store identifier queue descriptor properties
- [var storeIDs: [String]?](./storeids.md)
  An array containing the store identifiers found by the query used to create the queue descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerstorequeuedescriptor/startitemid)*