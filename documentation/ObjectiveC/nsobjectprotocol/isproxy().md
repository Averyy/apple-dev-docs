# isProxy()

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a Boolean value that indicates whether the receiver does not descend from [`NSObject`](../nsobject-swift.class.md).

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func isProxy() -> Bool
```

```objc
- (BOOL) isProxy;
```

## Return Value

[`NO`](../no.md) if the receiver really descends from [`NSObject`](../nsobject-swift.class.md), otherwise [`YES`](../yes.md).

## Discussion

This method is necessary because sending [`isKind(of:)`](./iskind%28of%29.md) or [`isMember(of:)`](./ismember%28of%29.md) to an [`NSProxy`](../../Foundation/nsproxy.md) object will test the object the proxy stands in for, not the proxy itself. Use this method to test if the receiver is a proxy (or a member of some other root class).


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobjectprotocol/isproxy())*