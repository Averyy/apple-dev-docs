# sortResults

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

An option to sort the results of a hit-test.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

> **Deprecated**: Use the [`searchMode`](./searchmode.md) option with value [`SCNHitTestSearchMode.all`](../scnhittestsearchmode/all.md) instead.

## Declaration

```swift
static let sortResults: SCNHitTestOption
```

```c
extern SCNHitTestOption const SCNHitTestSortResultsKey;
```

## Discussion

The value for this key is an [`NSNumber`](../../Foundation/nsnumber.md) object containing a Boolean value. The default value is [`true`](../../Swift/true.md), specifying that the array of hit-test results is sorted from nearest to farthest. (When using the [`hitTestWithSegment(from:to:options:)`](../scnnode/hittestwithsegment%28from,to,options%29.md) method, “nearest” is defined as closer to the point specified in the first parameter.) If you specify [`false`](../../Swift/false.md), results are returned in an arbitrary order.

## See Also

### Deprecated
- [static let firstFoundOnly: SCNHitTestOption](./firstfoundonly.md)
  An option to return only the first object found.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnhittestoption/sortresults)*