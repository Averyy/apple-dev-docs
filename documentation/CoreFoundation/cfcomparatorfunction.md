# CFComparatorFunction

**Framework**: Core Foundation  
**Kind**: typealias  
**Role**: Type Alias

Callback function that compares two values. You provide a pointer to this callback in certain Core Foundation sorting functions.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias CFComparatorFunction = (UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> CFComparisonResult
```

```c
typedef enum CFComparisonResult (*)(const void *, const void *, void *) CFComparatorFunction;
```

## Return Value

A `CFComparisonResult` value that indicates whether the `val1` is equal to, less than, or greater than `val2`. See [`CFComparisonResult`](./cfcomparisonresult.md) for a list of possible values.

## Discussion

If you need to sort the elements in a collection using special criteria, you can implement a comparator function with the signature defined by this prototype. You pass a pointer to this function in one of the “sort” functions, such as CFArray’s [`CFArraySortValues(_:_:_:_:)`](./cfarraysortvalues%28_,_,_,_%29.md).

You can also pass pointers to standard Core Foundation comparator functions such as [`CFStringCompare(_:_:_:)`](./cfstringcompare%28_,_,_%29.md) and [`CFDateCompare(_:_:_:)`](./cfdatecompare%28_,_,_%29.md).

## Parameters

- `val1`: The first value to compare.
- `val2`: The second value to compare.
- `context`: An untyped pointer to the context of the evaluation.

  The meaning of this value and its use are defined by each comparator function. This value is usually passed to a sort function, such as [`CFArraySortValues(_:_:_:_:)`](./cfarraysortvalues%28_,_,_,_%29.md), which then passes it, unchanged, to the comparator function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfcomparatorfunction)*