# isEqual(to:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Indicates whether the indexes in the receiving index set are the same indexes contained in another index set.

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
func isEqual(to indexSet: IndexSet) -> Bool
```

```objc
- (BOOL) isEqualToIndexSet:(NSIndexSet *) indexSet;
```

## Return Value

[`true`](../../Swift/true.md) when the indexes in the receiving index set are the same indexes `indexSet` contains, [`false`](../../Swift/false.md) otherwise.

## Parameters

- `indexSet`: Index set being inquired about.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexset/isequal(to:))*