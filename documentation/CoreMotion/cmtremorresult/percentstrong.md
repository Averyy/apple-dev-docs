# percentStrong

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The percentage of time when a tremor was likely, and the displacement amplitude was strong.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var percentStrong: Float { get }
```

```objc
@property (nonatomic, readonly) float percentStrong;
```

## See Also

### Accessing Tremor Data
- [var percentUnknown: Float](./percentunknown.md)
  The percentage of time when the algorithm couldn’t make a determination.
- [var percentNone: Float](./percentnone.md)
  The percentage of time when no tremor was detected.
- [var percentSlight: Float](./percentslight.md)
  The percentage of time when a tremor was likely, and the displacement amplitude was slight.
- [var percentMild: Float](./percentmild.md)
  The percentage of time when a tremor was likely, and the displacement amplitude was mild.
- [var percentModerate: Float](./percentmoderate.md)
  The percentage of time when a tremor was likely, and the displacement amplitude was moderate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmtremorresult/percentstrong)*