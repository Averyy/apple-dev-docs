# comparator

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) NSComparator comparator;
```

#### Discussion

Call this property only for sort descriptors initialized with [`init(key:ascending:comparator:)`](./init%28key,ascending,comparator%29.md).

## See Also

### Getting Information About a Sort Descriptor
- [var ascending: Bool](./ascending.md)
  A Boolean value that indicates whether the receiver specifies sorting in ascending order.
- [var key: String?](./key.md)
  The key that specifies the property to compare during sorting.
- [var keyPath: AnyKeyPath?](./keypath.md)
  The key path that specifies the property to compare during sorting.
- [var selector: Selector?](./selector.md)
  The selector for comparing objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssortdescriptor/comparator)*