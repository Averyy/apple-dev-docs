# insert(addingCount:at:initializingWith:)

**Framework**: Swift  
**Kind**: method

Inserts a given number of new items into this array at the specified position, using a callback to directly initialize array storage by populating an output span.

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
mutating func insert<E>(addingCount newItemCount: Int, at index: Int, initializingWith initializer: @_lifetime(0: copy 0) (inout OutputSpan<Element>) throws(E) -> Void) throws(E) where E : Error
```

#### Discussion

Existing elements in the array’s storage are moved towards the back as needed to make room for the new items.

If the array does not have sufficient capacity to hold the new elements, then this operation reallocates storage to extend its capacity, using a geometric growth rate.

```swift
var buffer = UniqueArray<Int>()
buffer.append([-999, 999])
var i = 0
buffer.insert(capacity: 3, at: 1) { target in
  while !target.isFull {
    target.append(i)
    i += 1
  }
}
// `buffer` now contains [-999, 0, 1, 2, 999]
```

> **Note**: O(`self.count` + `count`)

## Parameters

- `index`: The position at which to insert the new items. `index` must be a valid index in the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/insert(addingcount:at:initializingwith:))*