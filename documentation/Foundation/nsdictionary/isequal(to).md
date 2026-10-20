# isEqual(to:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the contents of the receiving dictionary are equal to the contents of another given dictionary.

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
func isEqual(to otherDictionary: [AnyHashable : Any]) -> Bool
```

```objc
- (BOOL) isEqualToDictionary:(NSDictionary<id,id> *) otherDictionary;
```

#### Return Value

[`true`](../../Swift/true.md) if the contents of `otherDictionary` are equal to the contents of the receiving dictionary, otherwise [`false`](../../Swift/false.md).

#### Discussion

Two dictionaries have equal contents if they each hold the same number of entries and, for a given key, the corresponding value objects in each dictionary satisfy the [`isEqual(_:)`](../../ObjectiveC/nsobjectprotocol/isequal%28_%29.md) test.

## Parameters

- `otherDictionary`: The dictionary with which to compare the receiving dictionary.

## See Also

### Related Documentation
- [func isEqual(Any?) -> Bool](../../ObjectiveC/nsobjectprotocol/isequal%28_%29.md)
  Returns a Boolean value that indicates whether the receiver and a given object are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/isequal(to:))*