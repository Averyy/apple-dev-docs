# dictionaryRepresentation()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a dictionary representation of the map table.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func dictionaryRepresentation() -> [AnyHashable : ObjectType]
```

```objc
- (NSDictionary<id,id> *) dictionaryRepresentation;
```

## Return Value

A dictionary representation of the map table.

## Discussion

The map table’s values and keys must conform to all the requirements specified in [`setObject(_:forKey:)`](../nsmutabledictionary/setobject%28_,forkey%29.md) in [`NSMutableDictionary`](../nsmutabledictionary.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmaptable/dictionaryrepresentation())*