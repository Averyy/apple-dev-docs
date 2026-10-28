# firstObjectCommon(with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the first object contained in the receiving array that’s equal to an object in another given array.

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
func firstObjectCommon(with otherArray: [Any]) -> Any?
```

```objc
- (ObjectType) firstObjectCommonWithArray:(NSArray<id> *) otherArray;
```

## Return Value

Returns the first object contained in the receiving array that’s equal to an object in `otherArray`. If no such object is found, returns `nil`.

## Discussion

This method uses [`isEqual(_:)`](../../ObjectiveC/nsobjectprotocol/isequal%28_%29.md) to check for object equality.

## Parameters

- `otherArray`: An array.

## See Also

### Related Documentation
- [func contains(Any) -> Bool](./contains%28_%29.md)
  Returns a Boolean value that indicates whether a given object is present in the array.
### Comparing Arrays
- [func isEqual(to: [Any]) -> Bool](./isequal%28to%29.md)
  Compares the receiving array to another array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/firstobjectcommon(with:))*