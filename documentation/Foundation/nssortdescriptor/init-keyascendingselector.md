# init(key:ascending:selector:)

**Framework**: Foundation  
**Kind**: init

Creates a sort descriptor with a specified string key path, ordering, and comparison selector.

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
init(key: String?, ascending: Bool, selector: Selector?)
```

#### Return Value

A sort descriptor that initializes with the specified key path, sort order, and comparison selector.

## Parameters

- `key`: For information about key paths, see  .
- `ascending`:   if the receiver specifies sorting in ascending order; otherwise,  .
- `selector`: The method to use when comparing the properties of objects, such as  . The selector must specify a method that you implement according to the value of the property that the key path identifies. Pass the selector a single parameter, the object to compare against, and it returns the appropriate   constant.

## See Also

- [init(key: String?, ascending: Bool)](nssortdescriptor/init(key:ascending:).md)
  Creates a sort descriptor with a specified string key path and sort order.
- [convenience init<Root, Value>(keyPath: KeyPath<Root, Value>, ascending: Bool)](nssortdescriptor/init(keypath:ascending:).md)
  Creates a sort descriptor with a specified key path and ordering.
- [init(key: String?, ascending: Bool, comparator: Comparator)](nssortdescriptor/init(key:ascending:comparator:).md)
  Creates a sort descriptor with a specified string key path and ordering, and a comparator block.
- [convenience init<Root, Value>(keyPath: KeyPath<Root, Value>, ascending: Bool, comparator: Comparator)](nssortdescriptor/init(keypath:ascending:comparator:).md)
  Creates a sort descriptor with a specified key path and ordering, and a comparator block.
- [init?(coder: NSCoder)](nssortdescriptor/init(coder:).md)
  Creates a sort descriptor by decoding from the coder you specify.
- [convenience init<Compared>(SortDescriptor<Compared>)](nssortdescriptor/init(_:)-7qf91.md)
  Creates a sort descriptor using a sort descriptor you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssortdescriptor/init(key:ascending:selector:))*