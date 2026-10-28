# isEqual(to:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Compares the receiving array to another array.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func isEqual(to otherArray: [Any]) -> Bool
```

```objc
- (BOOL) isEqualToArray:(NSArray<id> *) otherArray;
```

## Return Value

[`true`](../../Swift/true.md) if the contents of `otherArray` are equal to the contents of the receiving array, otherwise [`false`](../../Swift/false.md).

## Discussion

Two arrays have equal contents if they each hold the same number of objects and objects at a given index in each array satisfy the [`isEqual(_:)`](../../ObjectiveC/nsobjectprotocol/isequal%28_%29.md) test.

## Parameters

- `otherArray`: An array.

## See Also

### Comparing Arrays
- [func firstObjectCommon(with: [Any]) -> Any?](./firstobjectcommon%28with%29.md)
  Returns the first object contained in the receiving array that’s equal to an object in another given array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/isequal(to:))*