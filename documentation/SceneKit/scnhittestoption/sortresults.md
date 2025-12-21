# sortResults

**Framework**: SceneKit  
**Kind**: property

An option to sort the results of a hit-test.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static let sortResults: SCNHitTestOption
```

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing a Boolean value. The default value is [`true`](https://developer.apple.com/documentation/Swift/true), specifying that the array of hit-test results is sorted from nearest to farthest. (When using the [`hitTestWithSegment(from:to:options:)`](scnnode/hittestwithsegment(from:to:options:).md) method, “nearest” is defined as closer to the point specified in the first parameter.) If you specify [`false`](https://developer.apple.com/documentation/Swift/false), results are returned in an arbitrary order.

## See Also

- [static let firstFoundOnly: SCNHitTestOption](scnhittestoption/firstfoundonly.md)
  An option to return only the first object found.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnhittestoption/sortresults)*