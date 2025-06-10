# Dictionary

**Framework**: Swift  
**Kind**: struct

A collection whose elements are key-value pairs.

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
@frozen
struct Dictionary<Key, Value> where Key : Hashable
```

#### Overview

A dictionary is a type of hash table, providing fast access to the entries it contains. Each entry in the table is identified using its key, which is a hashable type such as a string or number. You use that key to retrieve the corresponding value, which can be any object. In other languages, similar data types are known as hashes or associated arrays.

Create a new dictionary by using a dictionary literal. A dictionary literal is a comma-separated list of key-value pairs, in which a colon separates each key from its associated value, surrounded by square brackets. You can assign a dictionary literal to a variable or constant or pass it to a function that expects a dictionary.

Here’s how you would create a dictionary of HTTP response codes and their related messages:

```swift
var responseMessages = [200: "OK",
                        403: "Access forbidden",
                        404: "File not found",
                        500: "Internal server error"]
```

The `responseMessages` variable is inferred to have type `[Int: String]`. The `Key` type of the dictionary is `Int`, and the `Value` type of the dictionary is `String`.

To create a dictionary with no key-value pairs, use an empty dictionary literal (`[:]`).

```swift
var emptyDict: [String: String] = [:]
```

Any type that conforms to the `Hashable` protocol can be used as a dictionary’s `Key` type, including all of Swift’s basic types. You can use your own custom types as dictionary keys by making them conform to the `Hashable` protocol.

### Getting and Setting Dictionary Values

The most common way to access values in a dictionary is to use a key as a subscript. Subscripting with a key takes the following form:

```swift
print(responseMessages[200])
// Prints "Optional("OK")"
```

Subscripting a dictionary with a key returns an optional value, because a dictionary might not hold a value for the key that you use in the subscript.

The next example uses key-based subscripting of the `responseMessages` dictionary with two keys that exist in the dictionary and one that does not.

```swift
let httpResponseCodes = [200, 403, 301]
for code in httpResponseCodes {
    if let message = responseMessages[code] {
        print("Response \(code): \(message)")
    } else {
        print("Unknown response \(code)")
    }
}
// Prints "Response 200: OK"
// Prints "Response 403: Access forbidden"
// Prints "Unknown response 301"
```

You can also update, modify, or remove keys and values from a dictionary using the key-based subscript. To add a new key-value pair, assign a value to a key that isn’t yet a part of the dictionary.

```swift
responseMessages[301] = "Moved permanently"
print(responseMessages[301])
// Prints "Optional("Moved permanently")"
```

Update an existing value by assigning a new value to a key that already exists in the dictionary. If you assign `nil` to an existing key, the key and its associated value are removed. The following example updates the value for the `404` code to be simply “Not found” and removes the key-value pair for the `500` code entirely.

```swift
responseMessages[404] = "Not found"
responseMessages[500] = nil
print(responseMessages)
// Prints "[301: "Moved permanently", 200: "OK", 403: "Access forbidden", 404: "Not found"]"
```

In a mutable `Dictionary` instance, you can modify in place a value that you’ve accessed through a keyed subscript. The code sample below declares a dictionary called `interestingNumbers` with string keys and values that are integer arrays, then sorts each array in-place in descending order.

```swift
var interestingNumbers = ["primes": [2, 3, 5, 7, 11, 13, 17],
                          "triangular": [1, 3, 6, 10, 15, 21, 28],
                          "hexagonal": [1, 6, 15, 28, 45, 66, 91]]
for key in interestingNumbers.keys {
    interestingNumbers[key]?.sort(by: >)
}

print(interestingNumbers["primes"]!)
// Prints "[17, 13, 11, 7, 5, 3, 2]"
```

### Iterating Over the Contents of a Dictionary

Every dictionary is an unordered collection of key-value pairs. You can iterate over a dictionary using a `for`-`in` loop, decomposing each key-value pair into the elements of a tuple.

```swift
let imagePaths = ["star": "/glyphs/star.png",
                  "portrait": "/images/content/portrait.jpg",
                  "spacer": "/images/shared/spacer.gif"]

for (name, path) in imagePaths {
    print("The path to '\(name)' is '\(path)'.")
}
// Prints "The path to 'star' is '/glyphs/star.png'."
// Prints "The path to 'portrait' is '/images/content/portrait.jpg'."
// Prints "The path to 'spacer' is '/images/shared/spacer.gif'."
```

The order of key-value pairs in a dictionary is stable between mutations but is otherwise unpredictable. If you need an ordered collection of key-value pairs and don’t need the fast key lookup that `Dictionary` provides, see the `KeyValuePairs` type for an alternative.

You can search a dictionary’s contents for a particular value using the `contains(where:)` or `firstIndex(where:)` methods supplied by default implementation. The following example checks to see if `imagePaths` contains any paths in the `"/glyphs"` directory:

```swift
let glyphIndex = imagePaths.firstIndex(where: { $0.value.hasPrefix("/glyphs") })
if let index = glyphIndex {
    print("The '\(imagePaths[index].key)' image is a glyph.")
} else {
    print("No glyphs found!")
}
// Prints "The 'star' image is a glyph."
```

Note that in this example, `imagePaths` is subscripted using a dictionary index. Unlike the key-based subscript, the index-based subscript returns the corresponding key-value pair as a non-optional tuple.

```swift
print(imagePaths[glyphIndex!])
// Prints "(key: "star", value: "/glyphs/star.png")"
```

A dictionary’s indices stay valid across additions to the dictionary as long as the dictionary has enough capacity to store the added values without allocating more buffer. When a dictionary outgrows its buffer, existing indices may be invalidated without any notification.

When you know how many new values you’re adding to a dictionary, use the `init(minimumCapacity:)` initializer to allocate the correct amount of buffer.

### Bridging Between Dictionary and Nsdictionary

You can bridge between `Dictionary` and `NSDictionary` using the `as` operator. For bridging to be possible, the `Key` and `Value` types of a dictionary must be classes, `@objc` protocols, or types that bridge to Foundation types.

Bridging from `Dictionary` to `NSDictionary` always takes O(1) time and space. When the dictionary’s `Key` and `Value` types are neither classes nor `@objc` protocols, any required bridging of elements occurs at the first access of each element. For this reason, the first operation that uses the contents of the dictionary may take O().

Bridging from `NSDictionary` to `Dictionary` first calls the `copy(with:)` method (`- copyWithZone:` in Objective-C) on the dictionary to get an immutable copy and then performs additional Swift bookkeeping work that takes O(1) time. For instances of `NSDictionary` that are already immutable, `copy(with:)` usually returns the same dictionary in O(1) time; otherwise, the copying performance is unspecified. The instances of `NSDictionary` and `Dictionary` share buffer using the same copy-on-write optimization that is used when two instances of `Dictionary` share buffer.

## Topics

### Creating a Dictionary
- [init()](dictionary/init.md)
  Creates an empty dictionary.
- [init(minimumCapacity: Int)](dictionary/init(minimumcapacity:).md)
  Creates an empty dictionary with preallocated space for at least the specified number of elements.
- [init<S>(uniqueKeysWithValues: S)](dictionary/init(uniquekeyswithvalues:).md)
  Creates a new dictionary from the key-value pairs in the given sequence.
- [init<S>(S, uniquingKeysWith: (Value, Value) throws -> Value) rethrows](dictionary/init(_:uniquingkeyswith:).md)
  Creates a new dictionary from the key-value pairs in the given sequence, using a combining closure to determine the value for any duplicate keys.
- [init<S>(grouping: S, by: (S.Element) throws -> Key) rethrows](dictionary/init(grouping:by:).md)
  Creates a new dictionary whose keys are the groupings returned by the given closure and whose values are arrays of the elements that returned each key.
### Inspecting a Dictionary
- [var isEmpty: Bool](dictionary/isempty.md)
  A Boolean value that indicates whether the dictionary is empty.
- [var count: Int](dictionary/count.md)
  The number of key-value pairs in the dictionary.
- [var capacity: Int](dictionary/capacity.md)
  The total number of key-value pairs that the dictionary can contain without allocating new storage.
### Accessing Keys and Values
- [subscript(Key) -> Value?](dictionary/subscript(_:)-8rfql.md)
  Accesses the value associated with the given key for reading and writing.
- [subscript(Key, default _: @autoclosure () -> Value) -> Value](dictionary/subscript(_:default:).md)
  Accesses the value with the given key, falling back to the given default value if the key isn’t found.
- [func index(forKey: Key) -> Dictionary<Key, Value>.Index?](dictionary/index(forkey:).md)
  Returns the index for the given key.
- [subscript(Dictionary<Key, Value>.Index) -> Dictionary<Key, Value>.Element](dictionary/subscript(_:)-4bhoo.md)
  Accesses the key-value pair at the specified position.
- [var keys: Dictionary<Key, Value>.Keys](dictionary/keys-swift.property.md)
  A collection containing just the keys of the dictionary.
- [var values: Dictionary<Key, Value>.Values](dictionary/values-swift.property.md)
  A collection containing just the values of the dictionary.
- [var first: Self.Element?](dictionary/first.md)
  The first element of the collection.
- [func randomElement() -> Self.Element?](dictionary/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](dictionary/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
### Adding Keys and Values
- [func updateValue(Value, forKey: Key) -> Value?](dictionary/updatevalue(_:forkey:).md)
  Updates the value stored in the dictionary for the given key, or adds a new key-value pair if the key does not exist.
- [func merge([Key : Value], uniquingKeysWith: (Value, Value) throws -> Value) rethrows](dictionary/merge(_:uniquingkeyswith:)-m2ub.md)
  Merges the given dictionary into this dictionary, using a combining closure to determine the value for any duplicate keys.
- [func merge<S>(S, uniquingKeysWith: (Value, Value) throws -> Value) rethrows](dictionary/merge(_:uniquingkeyswith:)-7smbb.md)
  Merges the key-value pairs in the given sequence into the dictionary, using a combining closure to determine the value for any duplicate keys.
- [func merging([Key : Value], uniquingKeysWith: (Value, Value) throws -> Value) rethrows -> [Key : Value]](dictionary/merging(_:uniquingkeyswith:)-3vtfs.md)
  Creates a dictionary by merging the given dictionary into this dictionary, using a combining closure to determine the value for duplicate keys.
- [func merging<S>(S, uniquingKeysWith: (Value, Value) throws -> Value) rethrows -> [Key : Value]](dictionary/merging(_:uniquingkeyswith:)-9bik6.md)
  Creates a dictionary by merging key-value pairs in a sequence into the dictionary, using a combining closure to determine the value for duplicate keys.
- [func reserveCapacity(Int)](dictionary/reservecapacity(_:).md)
  Reserves enough space to store the specified number of key-value pairs.
### Removing Keys and Values
- [func filter((Dictionary<Key, Value>.Element) throws -> Bool) rethrows -> [Key : Value]](dictionary/filter(_:).md)
  Returns a new dictionary containing the key-value pairs of the dictionary that satisfy the given predicate.
- [func removeValue(forKey: Key) -> Value?](dictionary/removevalue(forkey:).md)
  Removes the given key and its associated value from the dictionary.
- [func remove(at: Dictionary<Key, Value>.Index) -> Dictionary<Key, Value>.Element](dictionary/remove(at:).md)
  Removes and returns the key-value pair at the specified index.
- [func removeAll(keepingCapacity: Bool)](dictionary/removeall(keepingcapacity:).md)
  Removes all key-value pairs from the dictionary.
### Comparing Dictionaries
- [static func == ([Key : Value], [Key : Value]) -> Bool](dictionary/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](dictionary/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Iterating over Keys and Values
- [func forEach((Self.Element) throws -> Void) rethrows](dictionary/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func enumerated() -> EnumeratedSequence<Self>](dictionary/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [var lazy: LazySequence<Self>](dictionary/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
- [func makeIterator() -> Dictionary<Key, Value>.Iterator](dictionary/makeiterator.md)
  Returns an iterator over the dictionary’s key-value pairs.
- [var underestimatedCount: Int](dictionary/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Finding Elements
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](dictionary/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](dictionary/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](dictionary/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](dictionary/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](dictionary/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](dictionary/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
### Transforming a Dictionary
- [func mapValues<T>((Value) throws -> T) rethrows -> Dictionary<Key, T>](dictionary/mapvalues(_:).md)
  Returns a new dictionary containing the keys of this dictionary with the values transformed by the given closure.
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](dictionary/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](dictionary/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](dictionary/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func compactMapValues<T>((Value) throws -> T?) rethrows -> Dictionary<Key, T>](dictionary/compactmapvalues(_:).md)
  Returns a new dictionary containing only the key-value pairs that have non-`nil` values as the result of transformation by the given closure.
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](dictionary/flatmap(_:)-i3ly.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](dictionary/flatmap(_:)-6chv9.md)
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](dictionary/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func shuffled() -> [Self.Element]](dictionary/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](dictionary/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
### Performing Collection Operations
- [Order Dependent Operations on Dictionary](order-dependent-operations-on-dictionary.md)
  Perform order-dependent operations common to all collections, as implemented for `Dictionary`.
### Encoding and Decoding
- [func encode(to: any Encoder) throws](dictionary/encode(to:).md)
  Encodes the contents of this dictionary into the given encoder.
- [init(from: any Decoder) throws](dictionary/init(from:)-6e6js.md)
  Creates a new dictionary by decoding from the given decoder.
### Describing a Dictionary
- [var description: String](dictionary/description.md)
  A string that represents the contents of the dictionary.
- [var debugDescription: String](dictionary/debugdescription.md)
  A string that represents the contents of the dictionary, suitable for debugging.
- [var customMirror: Mirror](dictionary/custommirror.md)
  A mirror that reflects the dictionary.
- [func hash(into: inout Hasher)](dictionary/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Using a Dictionary as a Data Value
- [init?(from: MLDataValue.DictionaryType)](dictionary/init(from:)-5zhfu.md)
### Reference Types
- [class NSDictionary](../Foundation/NSDictionary.md)
  A static collection of objects associated with unique keys.
- [class NSMutableDictionary](../Foundation/NSMutableDictionary.md)
  A dynamic collection of objects associated with unique keys.
### Supporting Types
- [Dictionary.Keys](dictionary/keys-swift.struct.md)
  A view of a dictionary’s keys.
- [Dictionary.Values](dictionary/values-swift.struct.md)
  A view of a dictionary’s values.
- [Dictionary.Index](dictionary/index.md)
  The position of a key-value pair in a dictionary.
- [Dictionary.Indices](dictionary/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [Dictionary.Iterator](dictionary/iterator.md)
  An iterator over the members of a `Dictionary<Key, Value>`.
### Converting Between Dictionaries and Create ML Types
- [init?(from: MLDataValue)](dictionary/init(from:)-a452.md)
  Creates an instance of the conforming type from a data value.
- [var dataValue: MLDataValue](dictionary/datavalue.md)
  The value of the conforming type’s instance wrapped in a data value.
- [static var dataValueType: MLDataValue.ValueType](dictionary/datavaluetype.md)
  The underlying type the conforming type uses when it wraps itself in a data value.
### Creating a Dictionary from an Attribute Container
- [init<S>(AttributeContainer, including: S.Type) throws](dictionary/init(_:including:)-7afz2.md)
- [init<S>(AttributeContainer, including: KeyPath<AttributeScopes, S.Type>) throws](dictionary/init(_:including:)-8ls7v.md)
- [init(AttributeContainer)](dictionary/init(_:).md)
### Infrequently Used Functionality
- [init(dictionaryLiteral: (Key, Value)...)](dictionary/init(dictionaryliteral:).md)
  Creates a dictionary initialized with a dictionary literal.
- [var hashValue: Int](dictionary/hashvalue.md)
  The hash value.
### Type Aliases
- [Dictionary.Element](dictionary/element.md)
  The element type of a dictionary: a tuple containing an individual key-value pair.
### Default Implementations
- [Collection Implementations](dictionary/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](dictionary/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](dictionary/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](dictionary/customstringconvertible-implementations.md)
- [Decodable Implementations](dictionary/decodable-implementations.md)
- [Encodable Implementations](dictionary/encodable-implementations.md)
- [Equatable Implementations](dictionary/equatable-implementations.md)
- [ExpressibleByDictionaryLiteral Implementations](dictionary/expressiblebydictionaryliteral-implementations.md)
- [Hashable Implementations](dictionary/hashable-implementations.md)
- [MLDataValueConvertible Implementations](dictionary/mldatavalueconvertible-implementations.md)
- [Sequence Implementations](dictionary/sequence-implementations.md)

## Relationships

### Conforms To
- [CVarArg](cvararg.md)
- [Collection](collection.md)
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [CustomReflectable](customreflectable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [Decodable](decodable.md)
- [Encodable](encodable.md)
- [Equatable](equatable.md)
- [ExpressibleByDictionaryLiteral](expressiblebydictionaryliteral.md)
- [Hashable](hashable.md)
- [MLDataValueConvertible](../CreateML/MLDataValueConvertible.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
- [Sequence](sequence.md)

## See Also

- [struct Int](int.md)
  A signed integer value type.
- [struct Double](double.md)
  A double-precision, floating-point value type.
- [struct String](string.md)
  A Unicode string value that is a collection of characters.
- [struct Array](array.md)
  An ordered, random-access collection.
- [Swift Standard Library](swift-standard-library.md)
  Solve complex problems and write high-performance, readable code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dictionary)*