# prefix(_:)

**Framework**: Translation  
**Kind**: method

Returns an asynchronous sequence, up to the specified maximum length, containing the initial elements of the base asynchronous sequence.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func prefix(_ count: Int) -> AsyncPrefixSequence<Self>
```

#### Return Value

An asynchronous sequence starting at the beginning of the base sequence with at most `count` elements.

#### Discussion

Use `prefix(_:)` to reduce the number of elements produced by the asynchronous sequence.

In this example, an asynchronous sequence called `Counter` produces `Int` values from `1` to `10`. The `prefix(_:)` method causes the modified sequence to pass through the first six values, then end.

```swift
for await number in Counter(howHigh: 10).prefix(6) {
    print(number, terminator: " ")
}
// Prints "1 2 3 4 5 6 "
```

If the count passed to `prefix(_:)` exceeds the number of elements in the base sequence, the result contains all of the elements in the sequence.

## Parameters

- `count`: The maximum number of elements to return. The value of    must be greater than or equal to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/batchresponse/prefix(_:))*