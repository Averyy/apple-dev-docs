# init(_:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Creates an array containing the elements of a sequence.

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
init<S>(_ s: S) where Element == S.Element, S : Sequence
```

## Discussion

You can use this initializer to create an array from any other type that conforms to the `Sequence` protocol. For example, you might want to create an array with the integers from 1 through 7. Use this initializer around a range instead of typing all those numbers in an array literal.

```swift
let numbers = Array(1...7)
print(numbers)
// Prints "[1, 2, 3, 4, 5, 6, 7]"
```

You can also use this initializer to convert a complex sequence or collection type back to an array. For example, the `keys` property of a dictionary isn’t an array with its own storage, it’s a collection that maps its elements from the dictionary only when they’re accessed, saving the time and space needed to allocate an array. If you need to pass those keys to a method that takes an array, however, use this initializer to convert that list from its type of `LazyMapCollection<Dictionary<String, Int>, Int>` to a simple `[String]`.

```swift
func cacheImagesWithNames(names: [String]) {
    // custom image loading and caching
 }

let namedHues: [String: Int] = ["Vermillion": 18, "Magenta": 302,
        "Gold": 50, "Cerise": 320]
let colorNames = Array(namedHues.keys)
cacheImagesWithNames(colorNames)

print(colorNames)
// Prints "["Gold", "Cerise", "Magenta", "Vermillion"]"
```

## Parameters

- `s`: The sequence of elements to turn into an array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/contiguousarray/init(_:))*