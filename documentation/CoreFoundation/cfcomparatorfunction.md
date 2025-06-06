# CFComparatorFunction

**Framework**: Core Foundation  
**Kind**: typealias

Callback function that compares two values. You provide a pointer to this callback in certain Core Foundation sorting functions.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias CFComparatorFunction = (UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> CFComparisonResult
```

#### Return Value

A `CFComparisonResult` value that indicates whether the `val1` is equal to, less than, or greater than `val2`. See [`CFComparisonResult`](cfcomparisonresult.md) for a list of possible values.

#### Discussion

If you need to sort the elements in a collection using special criteria, you can implement a comparator function with the signature defined by this prototype. You pass a pointer to this function in one of the “sort” functions, such as CFArray’s [`CFArraySortValues(_:_:_:_:)`](cfarraysortvalues(_:_:_:_:).md).

You can also pass pointers to standard Core Foundation comparator functions such as [`CFStringCompare(_:_:_:)`](cfstringcompare(_:_:_:).md) and [`CFDateCompare(_:_:_:)`](cfdatecompare(_:_:_:).md).

## Parameters

- `val1`: The first value to compare.
- `val2`: The second value to compare.
- `context`: The meaning of this value and its use are defined by each comparator function. This value is usually passed to a sort function, such as  , which then passes it, unchanged, to the comparator function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcomparatorfunction)*