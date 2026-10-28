# percentUnknown

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The percentage of time when the algorithm couldn’t make a determination.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var percentUnknown: Float { get }
```

```objc
@property (nonatomic, readonly) float percentUnknown;
```

## Discussion

Both active motion and low signal level can cause `percentUnknown` results.

## See Also

### Accessing Tremor Data
- [var percentNone: Float](./percentnone.md)
  The percentage of time when no tremor was detected.
- [var percentSlight: Float](./percentslight.md)
  The percentage of time when a tremor was likely, and the displacement amplitude was slight.
- [var percentMild: Float](./percentmild.md)
  The percentage of time when a tremor was likely, and the displacement amplitude was mild.
- [var percentModerate: Float](./percentmoderate.md)
  The percentage of time when a tremor was likely, and the displacement amplitude was moderate.
- [var percentStrong: Float](./percentstrong.md)
  The percentage of time when a tremor was likely, and the displacement amplitude was strong.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmtremorresult/percentunknown)*