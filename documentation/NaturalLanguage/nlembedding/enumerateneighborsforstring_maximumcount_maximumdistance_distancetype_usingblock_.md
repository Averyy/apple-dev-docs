# enumerateNeighborsForString:maximumCount:maximumDistance:distanceType:usingBlock:

**Framework**: Natural Language  
**Kind**: method  
**Role**: Instance Method

Passes the nearest strings, within a radius of a string in the vocabulary, to a block.

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
- (void) enumerateNeighborsForString:(NSString *) string maximumCount:(NSUInteger) maxCount maximumDistance:(NLDistance) maxDistance distanceType:(NLDistanceType) distanceType usingBlock:(void (^)(NSString *neighbor, NLDistance distance, BOOL *stop)) block;
```

## Parameters

- `string`: A string in the embedding vocabulary.
- `maxCount`: The largest number of times the method calls `block`.
- `maxDistance`: The largest distance a neighbor can be from `string`.
- `distanceType`: A means of calculating distance that determines which formula the method uses to evaluate a neighbor’s distance from `string`.
- `block`: A block with the following parameters:

  - **`neighbor`**: A neighboring string.
  - **`distance`**: The distance from `string` to the neighboring string.
  - **`stop`**: A Boolean that indicates whether to stop enumerating neighbors.

## See Also

### Finding strings and their distances in an embedding
- [- neighborsForString:maximumCount:distanceType:](./neighborsforstring_maximumcount_distancetype_.md)
  Retrieves a limited number of strings near a string in the vocabulary.
- [- neighborsForString:maximumCount:maximumDistance:distanceType:](./neighborsforstring_maximumcount_maximumdistance_distancetype_.md)
  Retrieves a limited number of strings, within a radius of a string, in the vocabulary.
- [- neighborsForVector:maximumCount:distanceType:](./neighborsforvector_maximumcount_distancetype_.md)
  Retrieves a limited number of strings near a location in the vocabulary space.
- [- neighborsForVector:maximumCount:maximumDistance:distanceType:](./neighborsforvector_maximumcount_maximumdistance_distancetype_.md)
  Retrieves a limited number of strings within a radius of a location in the vocabulary space.
- [- enumerateNeighborsForString:maximumCount:distanceType:usingBlock:](./enumerateneighborsforstring_maximumcount_distancetype_usingblock_.md)
  Passes the nearest strings of a string in the vocabulary to a block.
- [- enumerateNeighborsForVector:maximumCount:distanceType:usingBlock:](./enumerateneighborsforvector_maximumcount_distancetype_usingblock_.md)
  Passes the nearest strings of a location in the vocabulary space to a closure.
- [- enumerateNeighborsForVector:maximumCount:maximumDistance:distanceType:usingBlock:](./enumerateneighborsforvector_maximumcount_maximumdistance_distancetype_usingblock_.md)
  Passes the nearest strings, within a radius of a location in the vocabulary space, to a block.
- [- distanceBetweenString:andString:distanceType:](./distancebetweenstring_andstring_distancetype_.md)
  Calculates the distance between two strings in the vocabulary space.
- [typealias NLDistance](../nldistance.md)
  The distance between two strings in a text embedding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlembedding/enumerateneighborsforstring:maximumcount:maximumdistance:distancetype:usingblock:)*