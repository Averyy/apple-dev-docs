# init(objects:count:)

**Framework**: Foundation  
**Kind**: init

Creates and returns a set containing a specified number of objects from a given C array of objects.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(objects: UnsafePointer<AnyObject>, count cnt: Int)
```

#### Return Value

A new ordered set containing cnt objects from the list of objects specified by `objects`.

## Parameters

- `objects`: If the same object appears more than once in objects, it is added only once to the returned ordered set. Each object receives a retain message as it is added to the set.
- `cnt`: The number of objects from objects to add to the new set.

## See Also

- [convenience init(orderedSet: NSOrderedSet, copyItems: Bool)](nsorderedset/init(orderedset:copyitems:).md)
  Initializes a new ordered set with the contents of a set, optionally copying the items.
- [convenience init(orderedSet: NSOrderedSet)](nsorderedset/init(orderedset:).md)
  Initializes a new ordered set with the contents of a set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedset/init(objects:count:)-3ny0m)*