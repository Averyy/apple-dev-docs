# init(_:)

**Framework**: Foundation  
**Kind**: init

Creates a sort descriptor using a sort descriptor you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
convenience init<Compared>(_ sortDescriptor: SortDescriptor<Compared>)
```

## Parameters

- `sortDescriptor`: A sort descriptor.

## See Also

- [init(key: String?, ascending: Bool)](nssortdescriptor/init(key:ascending:).md)
  Creates a sort descriptor with a specified string key path and sort order.
- [init(key: String?, ascending: Bool, selector: Selector?)](nssortdescriptor/init(key:ascending:selector:).md)
  Creates a sort descriptor with a specified string key path, ordering, and comparison selector.
- [convenience init<Root, Value>(keyPath: KeyPath<Root, Value>, ascending: Bool)](nssortdescriptor/init(keypath:ascending:).md)
  Creates a sort descriptor with a specified key path and ordering.
- [init(key: String?, ascending: Bool, comparator: Comparator)](nssortdescriptor/init(key:ascending:comparator:).md)
  Creates a sort descriptor with a specified string key path and ordering, and a comparator block.
- [convenience init<Root, Value>(keyPath: KeyPath<Root, Value>, ascending: Bool, comparator: Comparator)](nssortdescriptor/init(keypath:ascending:comparator:).md)
  Creates a sort descriptor with a specified key path and ordering, and a comparator block.
- [init?(coder: NSCoder)](nssortdescriptor/init(coder:).md)
  Creates a sort descriptor by decoding from the coder you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssortdescriptor/init(_:)-7qf91)*