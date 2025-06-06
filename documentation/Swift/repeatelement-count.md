# repeatElement(_:count:)

**Framework**: Swift  
**Kind**: func

Creates a collection containing the specified number of the given element.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func repeatElement<T>(_ element: T, count n: Int) -> Repeated<T>
```

#### Return Value

A collection that contains `count` elements that are all `element`.

#### Discussion

The following example creates a `Repeated<Int>` collection containing five zeroes:

```swift
let zeroes = repeatElement(0, count: 5)
for x in zeroes {
    print(x)
}
// 0
// 0
// 0
// 0
// 0
```

## Parameters

- `element`: The element to repeat.

## See Also

- [struct CollectionOfOne](collectionofone.md)
  A collection containing a single element.
- [struct EmptyCollection](emptycollection.md)
  A collection whose element type is `Element` but that is always empty.
- [struct KeyValuePairs](keyvaluepairs.md)
  A lightweight collection of key-value pairs.
- [typealias DictionaryLiteral](dictionaryliteral.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/repeatelement(_:count:))*