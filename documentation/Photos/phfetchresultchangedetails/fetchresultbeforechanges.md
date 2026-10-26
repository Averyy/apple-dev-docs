# fetchResultBeforeChanges

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The original fetch result, without recent changes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var fetchResultBeforeChanges: PHFetchResult<ObjectType> { get }
```

```objc
@property (atomic, strong, readonly) PHFetchResult<PHObject *> * fetchResultBeforeChanges;
```

#### Discussion

This property’s value is the same object you passed to the [`changeDetails(for:)`](../phchange/changedetails%28for%29-33a6n.md) method to request change details.

## See Also

### Getting the Changed Fetch Result
- [var fetchResultAfterChanges: PHFetchResult<ObjectType>](./fetchresultafterchanges.md)
  The current fetch result, incorporating recent changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phfetchresultchangedetails/fetchresultbeforechanges)*