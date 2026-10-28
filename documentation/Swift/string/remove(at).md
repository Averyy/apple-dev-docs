# remove(at:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Removes and returns the character at the specified position.

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
@discardableResult
mutating func remove(at i: String.Index) -> Character
```

## Return Value

The character that was removed.

## Discussion

All the elements following `i` are moved to close the gap. This example removes the hyphen from the middle of a string.

```swift
var nonempty = "non-empty"
if let i = nonempty.firstIndex(of: "-") {
    nonempty.remove(at: i)
}
print(nonempty)
// Prints "nonempty"
```

Calling this method invalidates any existing indices for use with this string.

## Parameters

- `i`: The position of the character to remove. `i` must be a valid index of the string that is not equal to the string’s end index.

## See Also

### Removing Substrings
- [func remove(at: Self.Index) -> Self.Element](./remove%28at%29-5g0wm.md)
  Removes and returns the element at the specified position.
- [func removeAll(keepingCapacity: Bool)](./removeall%28keepingcapacity%29.md)
  Replaces this string with the empty string.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](./removeall%28where%29.md)
  Removes all the elements that satisfy the given predicate.
- [func removeFirst() -> Self.Element](./removefirst%28%29.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](./removefirst%28_%29.md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeLast() -> Self.Element](./removelast%28%29.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](./removelast%28_%29.md)
  Removes the specified number of elements from the end of the collection.
- [func removeSubrange(Range<String.Index>)](./removesubrange%28_%29.md)
  Removes the characters in the given range.
- [func removeSubrange(Range<Self.Index>)](./removesubrange%28_%29-8maxn.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubrange<R>(R)](./removesubrange%28_%29-9twng.md)
  Removes the elements in the specified subrange from the collection.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](./drop%28while%29.md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](./dropfirst%28_%29.md)
  Returns a subsequence containing all but the given number of initial elements.
- [func dropLast(Int) -> Self.SubSequence](./droplast%28_%29.md)
  Returns a subsequence containing all but the specified number of final elements.
- [func popLast() -> Self.Element?](./poplast%28%29.md)
  Removes and returns the last element of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/remove(at:))*