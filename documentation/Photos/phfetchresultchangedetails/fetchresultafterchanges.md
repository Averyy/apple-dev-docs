# fetchResultAfterChanges

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The current fetch result, incorporating recent changes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var fetchResultAfterChanges: PHFetchResult<ObjectType> { get }
```

```objc
@property (atomic, strong, readonly) PHFetchResult<PHObject *> * fetchResultAfterChanges;
```

#### Discussion

You can use this object to inspect the current state of the fetched objects even if the [`hasIncrementalChanges`](./hasincrementalchanges.md) property’s value is `false`. Using this fetch result is equivalent to performing once more the same fetch that returned the original fetch result.

## See Also

### Getting the Changed Fetch Result
- [var fetchResultBeforeChanges: PHFetchResult<ObjectType>](./fetchresultbeforechanges.md)
  The original fetch result, without recent changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phfetchresultchangedetails/fetchresultafterchanges)*