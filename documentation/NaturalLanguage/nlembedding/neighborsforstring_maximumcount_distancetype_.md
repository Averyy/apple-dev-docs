# neighborsForString:maximumCount:distanceType:

**Framework**: Natural Language  
**Kind**: method  
**Role**: Instance Method

Retrieves a limited number of strings near a string in the vocabulary.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
- (NSArray<NSString *> *) neighborsForString:(NSString *) string maximumCount:(NSUInteger) maxCount distanceType:(NLDistanceType) distanceType;
```

#### Return Value

An array of neighboring strings.

## Parameters

- `string`: A string in the embedding vocabulary.
- `maxCount`: The largest number of neighboring strings that the method can return in an array.
- `distanceType`: A means of calculating distance that determines which formula the method uses to evaluate a neighbor’s distance from `string`.

## See Also

### Finding strings and their distances in an embedding
- [- neighborsForString:maximumCount:maximumDistance:distanceType:](./neighborsforstring_maximumcount_maximumdistance_distancetype_.md)
  Retrieves a limited number of strings, within a radius of a string, in the vocabulary.
- [- neighborsForVector:maximumCount:distanceType:](./neighborsforvector_maximumcount_distancetype_.md)
  Retrieves a limited number of strings near a location in the vocabulary space.
- [- neighborsForVector:maximumCount:maximumDistance:distanceType:](./neighborsforvector_maximumcount_maximumdistance_distancetype_.md)
  Retrieves a limited number of strings within a radius of a location in the vocabulary space.
- [- enumerateNeighborsForString:maximumCount:distanceType:usingBlock:](./enumerateneighborsforstring_maximumcount_distancetype_usingblock_.md)
  Passes the nearest strings of a string in the vocabulary to a block.
- [- enumerateNeighborsForString:maximumCount:maximumDistance:distanceType:usingBlock:](./enumerateneighborsforstring_maximumcount_maximumdistance_distancetype_usingblock_.md)
  Passes the nearest strings, within a radius of a string in the vocabulary, to a block.
- [- enumerateNeighborsForVector:maximumCount:distanceType:usingBlock:](./enumerateneighborsforvector_maximumcount_distancetype_usingblock_.md)
  Passes the nearest strings of a location in the vocabulary space to a closure.
- [- enumerateNeighborsForVector:maximumCount:maximumDistance:distanceType:usingBlock:](./enumerateneighborsforvector_maximumcount_maximumdistance_distancetype_usingblock_.md)
  Passes the nearest strings, within a radius of a location in the vocabulary space, to a block.
- [- distanceBetweenString:andString:distanceType:](./distancebetweenstring_andstring_distancetype_.md)
  Calculates the distance between two strings in the vocabulary space.
- [typealias NLDistance](../nldistance.md)
  The distance between two strings in a text embedding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlembedding/neighborsforstring:maximumcount:distancetype:)*