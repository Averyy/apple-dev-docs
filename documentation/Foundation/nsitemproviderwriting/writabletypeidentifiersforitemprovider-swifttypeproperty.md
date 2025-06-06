# writableTypeIdentifiersForItemProvider

**Framework**: Foundation  
**Kind**: property  
**Required**: Yes

An array of UTI strings representing the types of data that can be loaded for an item provider.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
static var writableTypeIdentifiersForItemProvider: [String] { get }
```

#### Discussion

Provide uniform type identifiers (UTIs) in order from highest fidelity to lowest. If your app employs a native data representation, place that first in the array.

Implement this version of the property to offer a minimal list of UTIs that  resulting item provider instances can support. For example, using this version of the property for an [`NSURL`](nsurl.md) object, your implementation should return the `public.url` UTI but not `public.file-url`.

Use the class version of this property when you do not initialize an item provider with an object, thereby deferring the underlying object’s instantiation until the destination app needs it.

## See Also

- [var writableTypeIdentifiersForItemProvider: [String]](nsitemproviderwriting/writabletypeidentifiersforitemprovider-swift.property.md)
  An array of UTI strings representing the types of data that can be loaded for an item provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemproviderwriting/writabletypeidentifiersforitemprovider-swift.type.property)*