# init(fromValue:)

**Framework**: HealthKit  
**Kind**: init

Returns an anchor object from the provided anchor value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(fromValue value: Int)
```

#### Return Value

An anchored object corresponding to the same sample as the anchor value.

#### Discussion

Prior to iOS 9.0, anchored object queries used anchor values to track the last sample returned by a previous query. Use this method to convert those anchor values into anchor objects.

## Parameters

- `value`: An anchor value.

## See Also

- [init(type: HKSampleType, predicate: NSPredicate?, anchor: HKQueryAnchor?, limit: Int, resultsHandler: (HKAnchoredObjectQuery, [HKSample]?, [HKDeletedObject]?, HKQueryAnchor?, (any Error)?) -> Void)](hkanchoredobjectquery/init(type:predicate:anchor:limit:resultshandler:).md)
  Initializes a new anchored object query.
- [init(type: HKSampleType, predicate: NSPredicate?, anchor: Int, limit: Int, completionHandler: (HKAnchoredObjectQuery, [HKSample]?, Int, (any Error)?) -> Void)](hkanchoredobjectquery/init(type:predicate:anchor:limit:completionhandler:).md)
  Initializes a new anchored object query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkqueryanchor/init(fromvalue:))*