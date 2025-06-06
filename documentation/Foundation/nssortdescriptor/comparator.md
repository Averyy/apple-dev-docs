# comparator

**Framework**: Foundation  
**Kind**: property

The comparator for the sort descriptor.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var comparator: Comparator { get }
```

#### Discussion

Call this property only for sort descriptors initialized with [`init(key:ascending:comparator:)`](nssortdescriptor/init(key:ascending:comparator:).md).

## See Also

- [var ascending: Bool](nssortdescriptor/ascending.md)
  A Boolean value that indicates whether the receiver specifies sorting in ascending order.
- [var key: String?](nssortdescriptor/key.md)
  The key that specifies the property to compare during sorting.
- [var keyPath: AnyKeyPath?](nssortdescriptor/keypath.md)
  The key path that specifies the property to compare during sorting.
- [var selector: Selector?](nssortdescriptor/selector.md)
  The selector for comparing objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssortdescriptor/comparator)*