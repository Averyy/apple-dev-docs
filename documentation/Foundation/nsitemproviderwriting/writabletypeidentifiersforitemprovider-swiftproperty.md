# writableTypeIdentifiersForItemProvider

**Framework**: Foundation  
**Kind**: property

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
optional var writableTypeIdentifiersForItemProvider: [String] { get }
```

#### Discussion

Provide uniform type identifiers (UTIs) in order from highest fidelity to lowest. If your app employs a native data representation, place that first in the array.

Use the instance version of this property when you initialize an item provider with an object. As possible, implement this property to provide an extended array of UTIs based on the object. For example, for an [`NSURL`](nsurl.md) object, your implementation could offer the `public.file-url` UTI, in addition to the `public.url` UTI, if your implementation detects that the stored URL uses the `file://` scheme.

## See Also

- [static var writableTypeIdentifiersForItemProvider: [String]](nsitemproviderwriting/writabletypeidentifiersforitemprovider-swift.type.property.md)
  An array of UTI strings representing the types of data that can be loaded for an item provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemproviderwriting/writabletypeidentifiersforitemprovider-swift.property)*