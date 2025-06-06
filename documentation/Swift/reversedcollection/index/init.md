# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a new index into a reversed collection for the position before the specified index.

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
init(_ base: Base.Index)
```

#### Discussion

When you create an index into a reversed collection using `base`, an index from the underlying collection, the resulting index is the position of the element  the element referenced by `base`. The following example creates a new `ReversedIndex` from the index of the `"a"` character in a string’s character view.

```swift
let name = "Horatio"
let aIndex = name.firstIndex(of: "a")!
// name[aIndex] == "a"

let reversedName = name.reversed()
let i = ReversedCollection<String>.Index(aIndex)
// reversedName[i] == "r"
```

The element at the position created using `ReversedIndex<...>(aIndex)` is `"r"`, the character before `"a"` in the `name` string.

## Parameters

- `base`: The position after the element to create an index for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/reversedcollection/index/init(_:))*