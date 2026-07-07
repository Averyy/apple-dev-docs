# append(addingCount:initializingWith:)

**Framework**: Swift  
**Kind**: method

Append a given number of items to the end of this array by populating an output span.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
mutating func append<E>(addingCount newItemCount: Int, initializingWith initializer: @_lifetime(0: copy 0) (inout OutputSpan<Element>) throws(E) -> Void) throws(E) where E : Error
```

#### Discussion

If the array does not have sufficient capacity to hold the requested number of new elements, then this reallocates the array’s storage to grow its capacity, using a geometric growth rate.

If the callback fails to fully populate its output span or if it throws an error, then the array keeps all items that were successfully initialized before the callback terminated the insertion.

> **Note**: O(`uninitializedCount`)

## Parameters

- `newItemCount`: The number of items to append to the array.
- `initializer`: A callback that gets called at most once to directly populate newly reserved storage within the array. The function is allowed to initialize fewer than `uninitializedCount` items. The array is appended however many items the callback adds to the output span before it returns (or before it throws an error).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/append(addingcount:initializingwith:))*