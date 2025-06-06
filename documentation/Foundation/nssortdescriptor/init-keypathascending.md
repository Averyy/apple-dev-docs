# init(keyPath:ascending:)

**Framework**: Foundation  
**Kind**: init

Creates a sort descriptor with a specified key path and ordering.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init<Root, Value>(keyPath: KeyPath<Root, Value>, ascending: Bool)
```

## Parameters

- `keyPath`: The key path to the property to compare.
- `ascending`: If  , the sort descriptor compares using the   sort order; otherwise, it uses  .

## See Also

- [init(key: String?, ascending: Bool)](nssortdescriptor/init(key:ascending:).md)
  Creates a sort descriptor with a specified string key path and sort order.
- [init(key: String?, ascending: Bool, selector: Selector?)](nssortdescriptor/init(key:ascending:selector:).md)
  Creates a sort descriptor with a specified string key path, ordering, and comparison selector.
- [init(key: String?, ascending: Bool, comparator: Comparator)](nssortdescriptor/init(key:ascending:comparator:).md)
  Creates a sort descriptor with a specified string key path and ordering, and a comparator block.
- [convenience init<Root, Value>(keyPath: KeyPath<Root, Value>, ascending: Bool, comparator: Comparator)](nssortdescriptor/init(keypath:ascending:comparator:).md)
  Creates a sort descriptor with a specified key path and ordering, and a comparator block.
- [init?(coder: NSCoder)](nssortdescriptor/init(coder:).md)
  Creates a sort descriptor by decoding from the coder you specify.
- [convenience init<Compared>(SortDescriptor<Compared>)](nssortdescriptor/init(_:)-7qf91.md)
  Creates a sort descriptor using a sort descriptor you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssortdescriptor/init(keypath:ascending:))*